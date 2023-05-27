from modules.ingredients_unit.repositories.ingredients_unit_repository import IngredientsUnitRepository

from utils.serializator.ingredients_unit import ingredientsUnitSerializator

class ListIngredientsUnitUseCase:
    def __init__(self,repository:IngredientsUnitRepository) -> None:
        self.repository = repository

    async def execute(self):
        try:
            units = await self.repository.findAll()

            data = []

            for unit in units:
                data.append(ingredientsUnitSerializator(ingredientsUnit=unit))

            return data
        except (ValueError):
            raise Exception(ValueError)