from shared.infra.prisma import prisma
from modules.dive.dtos.create_dive_dto import CreateDiveDTO

class DiveRepository:
    async def create(data:CreateDiveDTO):
        await prisma.connect()
        
        dive = await prisma.dive.create(data={
            "name": data.name,
            "description": data.description,
            "fileId": data.fileId,
            "userId": data.userId
        })

        await prisma.disconnect()

        return dive
    
    # async def enterDive(self, user_id: str, dive_id: str):
    #     await prisma.connect()
        
    #     # values = 
        
    #     await prisma.disconnect()

        # return values
    
    # async def exitDive(self, )