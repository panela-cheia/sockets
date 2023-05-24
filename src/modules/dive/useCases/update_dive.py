from modules.dive.repositories.dive_repository import DiveRepository
from modules.dive.dtos.update_dive_dto import UpdateDiveDTO

class UpdateDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository

    async def execute(self,updateDiveDTO:UpdateDiveDTO):
        verifyIfDiveNameAlreadyExists = await self.repository.findDiveByName(updateDiveDTO.name)


        if verifyIfDiveNameAlreadyExists:
            raise ValueError("This name has already been registered!")
        
        return await self.repository.update(updateDiveDTO=updateDiveDTO)