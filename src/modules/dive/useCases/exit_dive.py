from modules.dive.repositories.dive_repository import DiveRepository
from modules.dive.dtos.exit_dive_dto import ExitDiveDTO

class ExitDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository
    
    async def execute(self, data:ExitDiveDTO):
        # Verificar se o buteco a ser deixado existe
        exit_dive = await self.repository.findDiveById(data.diveId)
        if not exit_dive:
            raise ValueError("Dive does not exist")
        
        if exit_dive.owner == data.user and data.new_owner:
            verifyNewOwner = await self.repository.findById(id=data.new_owner)
            if not verifyNewOwner:
                raise ValueError("User does not exist")
            
            await self.repository.updateDiveOwner(data.user,data.new_owner)
        else:
            # Verificar se o usuário existe
            user = await self.repository.findById(id=data.user)
            if not user:
                raise ValueError("User does not exist")
            
            # Verificar se o usuário está tentando sair de um buteco que ele não está inserido
            existing_dive = await self.repository.verifyEntry(user=data.user, dive=data.diveId)

            if not existing_dive:
                raise ValueError("Not in this dive")
        
        await self.repository.exitDive(data.user, data.diveId)

        response = { "ok": "Successfully left the dive" }

        return response