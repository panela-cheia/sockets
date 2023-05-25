from modules.dive.repositories.dive_repository import DiveRepository

class EnterDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository
    
    async def execute(self, user_id: str, dive_id: str):
        
        # Verificar se o usuário existe
        user = await self.repository.findById(id=user_id)
        if not user:
            raise ValueError("User does not exist")
        
        # Verificar se o buteco a ser entrado existe
        enter_dive = await self.repository.findDiveById(dive_id)
        if not enter_dive:
            raise ValueError("Dive does not exist")
        
        # Verificar se o usuário está tentando entrar em um buteco que ele já está inserido
        existing_dive = await self.repository.verifyEntry(user=user_id, dive=dive_id)

        if existing_dive:
            raise ValueError("Already in this dive")
        

        # Criar o relacionamento
        await self.repository.enterDive(user_id, dive_id)

        return "Successfully joined the dive"