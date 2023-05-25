from shared.infra.prisma import prisma
from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO

class RecipeRepository:
    async def create(self, data:CreateRecipeDTO):
        await prisma.connect()

        recipe = await prisma.recipe.create(
            data={
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
            },
            include={
                "barn":True,
                "dive":True,
                "ingredients":True,
                "photo":True,
                "reactions":True,
                "user":True
            }
        )

        await prisma.disconnect()

        return recipe
    
    async def findAll(self):
        await prisma.connect()

        recipes = await prisma.recipe.find_many(
            where={},
            include={
                "barn":True,
                "dive":True,
                "ingredients":True,
                "photo":True,
                "reactions":True,
                "user":True
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
                "barn":True,
                "dive":True,
                "ingredients":True,
                "photo":True,
                "reactions":True,
                "user":True
            }
        )

        await prisma.disconnect()

        return recipes

    async def verify_existing_reaction(self,recipe_id:str,user_id:str):
        await prisma.connect()
        
        existing_reaction = await prisma.reaction.find_first(
            where={"recipeId": recipe_id, "userId": user_id}
        )

        await prisma.disconnect()
        
        return existing_reaction
    
    async def reaction(self,recipe_id:str,type:str,user_id:str):
        await prisma.connect()

        reaction = await prisma.reaction.create(
            data={
                "type": type,
                "recipeId": recipe_id,
                "userId": user_id
            }
        )

        await prisma.disconnect()

        return reaction
    
    async def updateReaction(self,id:str,type:str):
        await prisma.connect()

        reaction = await prisma.reaction.update(
                where={"id": id},
                data={"type": type}
            )

        await prisma.disconnect()

        return reaction

    async def getReactionQuantities(self, recipe_id: str):
        reaction_quantities = {
            "bão": 0,
            "mió de bão": 0,
            "água na boca": 0
        }

        try:    
            await prisma.connect()

            recipe_reactions = await prisma.reaction.find_many(
                where={"recipeId":recipe_id}
            )

            await prisma.disconnect()


            for reaction in recipe_reactions:
                if reaction.type in reaction_quantities:
                    reaction_quantities[reaction.type] += 1
        except (ValueError):
            # Lidar com exceção de consulta
            print(ValueError)

        return reaction_quantities