from shared.infra.prisma import prisma
from modules.dive.dtos.create_dive_dto import CreateDiveDTO
from modules.dive.dtos.update_dive_dto import UpdateDiveDTO

class DiveRepository:
    async def create(self, data:CreateDiveDTO):
        await prisma.connect()
        
        dive = await prisma.dive.create(
            data={
                "name":data.name,
                "description":data.description,
                "fileId":data.fileId,
                "ownerId":data.userId,
            },
            include={
                "members":True,
                "owner":True,
                "photo":True,
                "recipe":True
            }
        )

        await prisma.disconnect()

        return dive
    
    async def findById(self, id):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                "id": id
            },
            include={
                "ownersDive":True,
                "photo":True,
                "recipes":True
            }
        )

        await prisma.disconnect()

        return user

    async def findDiveById(self, dive_id):
        await prisma.connect()

        dive = await prisma.dive.find_unique(
            where={
                "id": dive_id
            },
            include={
                "owner":True,
                "photo":True,
                "recipe":{
                    "include":{
                        "barn":True,
                        "dive":True,
                        "ingredients":True,
                        "photo":True,
                        "reactions":True,
                        "user":{
                            "include":{
                                "photo":True
                            }
                        }
                    },
                    "order_by":{
                        "created_at":"desc"
                    }
                }
            }
        )

        await prisma.disconnect()

        return dive
    
    async def findDiveByName(self, name):
        await prisma.connect()

        dive = await prisma.dive.find_unique(
            where={
                "name": name
            },
            include={
                "ownersDive":True,
                "photo":True,
                "recipes":True
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
            },
            include={
                "dive":True,
                "user":True,
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
            },
            include={
                "dive":True,
                "user":True
            }
        )

        await prisma.disconnect()

    async def update(self,updateDiveDTO:UpdateDiveDTO):
        await prisma.connect()

        dive = await prisma.dive.update(
            where={
                "id": updateDiveDTO.id
            },
            data={
                "description":updateDiveDTO.description,
                "fileId":updateDiveDTO.fileId,
                "name":updateDiveDTO.name
            },
            include={
                "ownersDive":True,
                "photo":True,
                "recipes":True
            }
        )

        await prisma.disconnect()

        return dive
    
    async def findAll(self, name:str):
        await prisma.connect()

        dives = await prisma.dive.find_many(
            where={
                "name":{
                    "contains":name
                }
            },
            include={
                "owner":True,
                "photo":True,
                "recipe":True,
                "members":True
            }
        )

        await prisma.disconnect()

        return dives
    
    async def updateDiveOwner(self,dive_id:str,new_owner:str):
        await prisma.connect()

        dives = await prisma.dive.update(
            where={
                "id":dive_id
            },
            data={
                "ownersDive":new_owner
            }
        )

        await prisma.disconnect()
        return dives
    
    async def findUserDive(self,user_id):
        await prisma.connect()

        dives = await prisma.usersdive.find_many(
            where={
                "userId":{
                    "equals":user_id
                }
            },
            include={
                "dive":{
                    "include":{
                        "photo":True,
                        "recipe":{
                            "include":{
                                "photo":True
                            }
                        },
                        "members":{
                            "include":{
                                "user":True
                            }
                        },
                        
                    }
                },
                
                "user":{
                    "include":{
                        "photo":True
                    }
                }
            }
        )

        await prisma.disconnect()

        return dives