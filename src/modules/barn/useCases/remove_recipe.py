from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO
from modules.barn.repositories.barn_repository import BarnRepository


class RemoveRecipeUseCase:
    def __init__(self, repository: BarnRepository):
        self.repository = repository

    async def execute(self, data: RemoveRecipeDTO):
        barn =  await self.repository.removeRecipe(data=data)

        return barn