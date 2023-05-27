from modules.dive.repositories.dive_repository import DiveRepository
from modules.dive.dtos.update_dive_dto import UpdateDiveDTO

class UpdateDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository

    async def execute(self,updateDiveDTO:UpdateDiveDTO):
        verifyIfDiveNameAlreadyExists = await self.repository.findDiveByName(updateDiveDTO.name)

        if verifyIfDiveNameAlreadyExists:
            raise ValueError("This name has already been registered!")
        
        verifyIfDiveExists = await self.repository.findDiveById(dive_id=updateDiveDTO.id)

        if not verifyIfDiveExists:
            raise ValueError("This dive not exists!")

        try:
            if not updateDiveDTO.description:
                updateDiveDTO.description = verifyIfDiveExists.description

            await self.repository.update(updateDiveDTO=updateDiveDTO)
        except (ValueError):
            raise Exception(ValueError)
        
        data = { "ok": "dive updated successfully!" }

        return data