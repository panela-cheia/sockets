from modules.ingredients_unit.repositories.ingredients_unit_repository import IngredientsUnitRepository

from utils.serializator.ingredients_unit import ingredientsUnitSerializator

class CreateIngredientsUnitUseCase:
    def __init__(self,repository:IngredientsUnitRepository) -> None:
        self.repository = repository

    async def execute(self,name:str):

        try:
            verifyIfUnitAlreadyBeenRegistered = await self.repository.findByName(name=name)

            if verifyIfUnitAlreadyBeenRegistered:
                raise Exception("This name already been registered!")

            unit =  await self.repository.create(name=name)

            return ingredientsUnitSerializator(ingredientsUnit=unit)
        except (ValueError):
            raise Exception(ValueError)