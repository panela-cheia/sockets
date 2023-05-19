from modules.recipes.repositories.recipe_repository import RecipeRepository

class ListRecipesUseCase:
    def __init__(self,repository:RecipeRepository) -> None:
        self.repository = repository

    async def execute(self):
        recipes =  await self.repository.findAll()
        return recipes