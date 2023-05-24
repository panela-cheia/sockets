from modules.dive.repositories.dive_repository import DiveRepository

class ExitDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository
    
    async def execute(self, user_id: str, dive_id: str):
        # Verificar se o usuário existe
        user = await self.repository.findById(id=user_id)
        if not user:
            raise ValueError("User does not exist")

        # Verificar se o buteco a ser deixado existe
        exit_dive = await self.repository.findDiveById(dive_id)
        if not exit_dive:
            raise ValueError("Dive does not exist")
        
        # Verificar se o usuário está tentando sair de um buteco que ele não está inserido
        existing_dive = await self.repository.verifyEntry(user=user_id, dive=dive_id)

        if not existing_dive:
            raise ValueError("Not in this dive")
        
        await self.repository.exitDive(user_id, dive_id)

        return "Successfully left the dive"