from shared.infra.prisma import prisma
from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO

class RecipeRepository:
    async def create(self, data:CreateRecipeDTO):
        await prisma.connect()

        recipe = await prisma.recipe.create(data={
            "name": data.name,
            "description": data.description,
            "userId": data.userId,
            "diveId": data.diveId,
            "fileId": data.fileId,
            "ingredients": {
                "create": [
                    {
                        "name": ingredient.name,
                        "amount": ingredient.amount,
                        "unit": ingredient.unit

                    }
                    for ingredient in data.ingredients
                ]
            }   
        })

        await prisma.disconnect()

        return recipe
    
    async def findAll(self):
        await prisma.connect()

        recipes = await prisma.recipe.find_many(
            where={},
            include={
                "User":True,
                "photo":True,
                "ingredients":True,
                "dive":True
            }
        )

        await prisma.disconnect()

        return recipes

    async def search(self,name:str):
        await prisma.connect()

        recipes = await prisma.recipe.find_many(
            where={
                "name": {
                    "contains": name
                }
            },
            include={
                "User": True,
                "photo":True,
                "ingredients":True,
                "dive":True
            }
        )

        await prisma.disconnect()

        return recipes
