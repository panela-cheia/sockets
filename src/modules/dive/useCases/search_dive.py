from modules.dive.repositories.dive_repository import DiveRepository

class SearchDiveUseCase:
    def __init__(self, repository: DiveRepository):
        self.repository = repository

    async def execute(self, diveName: str):
        return await self.repository.findAll(name=diveName)