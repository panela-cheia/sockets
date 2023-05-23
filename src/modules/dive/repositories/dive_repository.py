from shared.infra.prisma import prisma
from modules.dive.dtos.create_dive_dto import CreateDiveDTO

class DiveRepository:
    async def create(self, data:CreateDiveDTO):
        await prisma.connect()
        
        dive = await prisma.dive.create(data={
            "name": data.name,
            "description": data.description,
            "fileId": data.fileId,
            "userId": data.userId
        })

        await prisma.disconnect()

        return dive
    
    async def findById(self, id):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                "id": id
            }
        )

        await prisma.disconnect()

        return user

    async def findDiveById(self, dive_id):
        await prisma.connect()

        dive = await prisma.dive.unique(
            where={
                "id": dive_id
            }
        )

        await prisma.disconnect()

        return dive
    
    async def verifyEntry(self, user: str, dive: str) -> bool:
        await prisma.connect()
        
        values = await prisma.usersdive.find_first(
            where={
                "userId": user,
                "diveId": dive
            }
        )
        
        await prisma.disconnect()

        return values is not None

    async def enterDive(self, user_id: str, dive_id: str):
        await prisma.connect()
        
        values = await prisma.usersdive.create(
            data={
                "user": {"connect":{"id": user_id}},
                "dive": {"connect":{"id": dive_id}}
            }
        )
        
        await prisma.disconnect()

        return values
    
    async def exitDive(self, user_id: str, dive_id: str):
        await prisma.connect()

        await prisma.usersdive.delete(
            where={
                "userId_diveId":{
                    "userId": user_id,
                    "diveId": dive_id
                }
            }
        )

        await prisma.disconnect()