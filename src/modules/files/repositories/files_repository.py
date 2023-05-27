from shared.infra.prisma import prisma

class FilesRepository:
    async def create(self,name:str,path:str):

        await prisma.connect()

        fileCreated = await prisma.file.create(
            data={
                "name":name,
                "path":path
            },
            include={
                "dive":True,
                "recipe":True,
                "user":True
            }
        )

        await prisma.disconnect()

        return fileCreated
        

    async def delete(self,id):
        await prisma.connect()

        await prisma.file.delete(
            where={
                "id":id
            },
            include={
                "dive":True,
                "recipe":True,
                "user":True
            }
        )

        await prisma.disconnect()


    async def findById(self,id):
        await prisma.connect()

        foundedFile = await prisma.file.find_unique(
            where={
                "id":id
            },
            include={
                "dive":True,
                "recipe":True,
                "user":True
            }
        )

        await prisma.disconnect()
        
        return foundedFile