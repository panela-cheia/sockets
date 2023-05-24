from modules.dive.dtos.create_dive_dto import CreateDiveDTO
from modules.dive.repositories.dive_repository import DiveRepository

class CreateDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository
    
    async def execute(self, data:CreateDiveDTO):
        dive = await self.repository.create(data)
        updated_dive = await self.repository.updateDiveOwner(dive.userId, dive.id)
        print(updated_dive)
        return updated_dive