from shared.infra.prisma import prisma

class UserRepository:
    async def create(self,name,username,email,password):
        await prisma.connect()

        user = await prisma.user.create(
            data={
                "name": name,
                "username": username,
                "email": email,
                "password": password
            }
        )

        await prisma.disconnect()

        return user

    async def findAll(self):
        await prisma.connect()

        users = await prisma.user.find_many()

        await prisma.disconnect()

        return users
    
    async def findByEmail(self,email):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                'email':email
            }
        )

        await prisma.disconnect()

        return user
    
    async def findByUsername(self,username):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                "username":username
            }
        )

        await prisma.disconnect()

        return user
    
    async def update(self,id,name,username,bio):
        await prisma.connect()

        user = await prisma.user.update(
            where={
                'id': id
            },
            data={
                "name":name,
                "username":username,
                "bio":bio,
                
            }
        )

        await prisma.disconnect()

        return user

    async def updatePhoto(self,id,photo):
        await prisma.connect()

        user = await prisma.user.update(
            where={
                'id': id
            },
            data={
                "photo":{
                    "connect":photo
                }
                
            }
        )

        await prisma.disconnect()

        return user
    
    async def delete(self,id):
        await prisma.connect()

        user = await prisma.user.delete(
            where={
                'id': id
            }
        )

        await prisma.disconnect()

        return user