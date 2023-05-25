from shared.infra.prisma import prisma

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO

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
            },
            include={
                "recipes":True,
                "user":{
                    "include":{
                        "photo":True
                    }
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
                "recipes":True,
                "user":True
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
            },
            include={
                "recipes":True,
                "user":True
            }
        )


        await prisma.disconnect()

        return barn