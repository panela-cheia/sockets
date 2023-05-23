from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.repositories.barn_repository import BarnRepository


class RemoveRecipeUseCase:
    def __init__(self, repository: BarnRepository):
        self.repository = repository

    async def execute(self, data: BarnSaveRecipeDTO):
        barn =  await self.repository.removeRecipe(data=data)

        return barn