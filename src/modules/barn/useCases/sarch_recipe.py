from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO
from modules.barn.repositories.barn_repository import BarnRepository


class SearhRecipeUseCase:
    def __init__(self, repository: BarnRepository):
        self.repository = repository

    async def execute(self, data: SearchRecipeInBarnDTO):
        barns =  await self.repository.findAll(barnId=data.barnId)

        if barns is None:
            return []
        
        recipes = []

        for recipe in barns.recipes:
            if data.recipeName in recipe.name:
                recipes.append(recipe)

        return recipes
    