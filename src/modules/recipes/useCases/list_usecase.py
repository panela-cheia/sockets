from modules.recipes.repositories.recipe_repository import RecipeRepository
from utils.serializator.recipe import recipeSerializator


class ListRecipesUseCase:
    def __init__(self, repository: RecipeRepository) -> None:
        self.repository = repository

    async def execute(self):
        recipes = await self.repository.findAll()

        all_recipes = []

        for recipe in recipes:
            reactions = await self.repository.getReactionQuantities(recipe_id=recipe.id)

            recipe_formatted =  recipeSerializator(recipe=recipe,reactions=reactions)

            all_recipes.append(recipe_formatted)

        return all_recipes