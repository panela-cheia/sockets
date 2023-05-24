from shared.infra.prisma import prisma

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO
from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO


class BarnRepository:

    async def save(self, data:BarnSaveRecipeDTO):

        await prisma.connect()

        barn = await prisma.barn.update(
            where={
                "id": data.barnId
            },
            data={
                "recipes":{
                    "connect": [{ "id":data.recipeId }]
                }
            }
        )


        await prisma.disconnect()

        return barn

    
    async def findAll(self, barnId:str):
        await prisma.connect()

        barns = await prisma.barn.find_first(
            where={
                "id": barnId
            },
            include={
                "recipes":True
            }
        )

        await prisma.disconnect()

        return barns
    
    async def removeRecipe(self, data:RemoveRecipeDTO):
        await prisma.connect()

        barn = await prisma.barn.update(
            where={
                "id": data.barnId
            },
            data={
                "recipes":{
                    "disconnect": [{ "id":data.recipeId }]
                }
            }
        )


        await prisma.disconnect()

        return barn