from shared.infra.prisma import prisma

class IngredientsUnitRepository:
    async def create(self,name:str):

        await prisma.connect()

        unit = await prisma.ingredientsunit.create(
            data={
                "name":name
            }
        )

        await prisma.disconnect()

        return unit
        

    async def delete(self,id):
        await prisma.connect()

        await prisma.ingredientsunit.delete(
            where={
                "id":id
            }
        )

        await prisma.disconnect()


    async def findAll(self):
        await prisma.connect()

        units = await prisma.ingredientsunit.find_many(
            where={
                
            },
            order={
                "name":"asc"
            }
        )

        await prisma.disconnect()
        
        return units
    
    async def findByName(self,name:str):
        await prisma.connect()

        units = await prisma.ingredientsunit.find_first(
            where={
                "name":{
                    "equals":name
                }
            }
        )

        await prisma.disconnect()
        
        return units
    
    async def findById(self,id:str):
        await prisma.connect()

        unit = await prisma.ingredientsunit.find_unique(
            where={
                "id":id
            }
        )

        await prisma.disconnect()

        return unit