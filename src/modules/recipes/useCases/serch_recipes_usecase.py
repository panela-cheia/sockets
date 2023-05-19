from modules.recipes.repositories.recipe_repository import RecipeRepository
from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO

class SearchRecipesUseCase:
    def __init__(self,repository:RecipeRepository) -> None:
        self.repository = repository

    async def execute(self,name:str):
        recipes =  await self.repository.search(name=name)
        return recipes