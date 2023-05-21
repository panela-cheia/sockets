from modules.dive.dtos.create_dive_dto import CreateDiveDTO
from modules.dive.repositories.dive_repository import DiveRepository

class CreateDiveUseCase:
    def __init__(self, repository: DiveRepository) -> None:
        self.repository = repository
    
    async def execute(self, data:CreateDiveDTO):
        return await self.repository.create(data=data) 