from modules.ingredients_unit.repositories.ingredients_unit_repository import IngredientsUnitRepository

class DeleleIngredientsUnitUseCase:
    def __init__(self,repository:IngredientsUnitRepository) -> None:
        self.repository = repository

    async def execute(self,id:str):

        try:
            verifyIfUnitAlreadyExists = await self.repository.findById(id=id)

            if not verifyIfUnitAlreadyExists:
                return { "error":"This unit not exits!" }

            await self.repository.delete(id=id)

            data = { "ok": "unit deleted successfully!" }

            return data
        except (ValueError):
            raise { "error":ValueError }