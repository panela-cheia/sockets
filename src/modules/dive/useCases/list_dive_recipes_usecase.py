from modules.dive.repositories.dive_repository import DiveRepository
from modules.recipes.repositories.recipe_repository import RecipeRepository

from utils.serializator.recipe import recipeSerializator

class ListDiveRecipesUseCase:
    def __init__(self, repository: DiveRepository,recipeRepository:RecipeRepository) -> None:
        self.repository = repository
        self.recipeRepository = recipeRepository
    
    async def execute(self, dive_id:str):
        dives = await self.repository.findDiveById(dive_id=dive_id)

        all_recipes = []

        for recipe in dives.recipe:
            reactions = await self.recipeRepository.getReactionQuantities(recipe_id=recipe.id)

            recipe_formatted =  recipeSerializator(recipe=recipe,reactions=reactions)

            all_recipes.append(recipe_formatted)

        return all_recipes