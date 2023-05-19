from shared.infra.prisma import prisma

from config.app_url import APP_URL

class FilesRepository:
    async def create(self,name:str,path:str):

        await prisma.connect()

        fileCreated = await prisma.file.create(data={
            "name":name,
            "path":path
        })

        await prisma.disconnect()

        return fileCreated
        

    async def delete(self,id):
        await prisma.connect()

        await prisma.file.delete(
            where={
                "id":id
            }
        )

        await prisma.disconnect()


    async def findById(self,id):
        await prisma.connect()

        await prisma.file.find_unique(
            where={
                "id":id
            }
        )

        await prisma.disconnect()