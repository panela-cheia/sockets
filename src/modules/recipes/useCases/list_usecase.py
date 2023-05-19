from modules.recipes.repositories.recipe_repository import RecipeRepository
from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO

class ListRecipesUseCase:
    def __init__(self,repository:RecipeRepository) -> None:
        self.repository = repository

    async def execute(self):
        recipes =  await self.repository.findAll()
        return recipes