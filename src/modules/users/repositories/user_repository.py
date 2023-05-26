from shared.infra.prisma import prisma


class UserRepository:
    async def create(self, name, username, email, password):
        await prisma.connect()

        user = await prisma.user.create(
            data={
                "name": name,
                "username": username,
                "email": email,
                "password": password
            }
        )

        await prisma.barn.create(
            data={
                "user": {
                    "connect": {
                        "id": user.id
                    }
                }
            }
        )

        await prisma.disconnect()

        return user

    async def findAll(self):
        await prisma.connect()

        users = await prisma.user.find_many(
            include={
                "barn": True,
                "followers":True,
                "following":True,
                "ownersDive":True,
                "photo":True,
                "reactions":True,
                "recipes":True,
                "usersDive":True
            }
        )

        await prisma.disconnect()

        return users

    async def findByEmail(self, email):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                'email': email
            }
        )

        await prisma.disconnect()

        return user

    async def findByUsername(self, username):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                "username": username
            },
            include={
                "barn": True,
                "followers":True,
                "following":True,
                "ownersDive":True,
                "photo":True,
                "reactions":True,
                "recipes":True,
                "usersDive":True
            }
        )

        await prisma.disconnect()

        return user

    async def findById(self, id):
        await prisma.connect()

        user = await prisma.user.find_unique(
            where={
                "id": id
            },
            include={
                "barn": True,
                "followers":True,
                "following":True,
                "ownersDive":True,
                "photo":True,
                "reactions":True,
                "recipes":True,
                "usersDive":True
            }
        )

        await prisma.disconnect()

        return user

    async def update(self, id, name, username, bio):
        await prisma.connect()

        user = await prisma.user.update(
            where={
                "id": id
            },
            data={
                "name": name,
                "username": username,
                "bio": bio
            }
        )

        await prisma.disconnect()

        return user

    async def updatePhoto(self, id, photo):
        await prisma.connect()

        user = await prisma.user.update(
            where={
                'id': id
            },
            data={
                "photo": {
                    "connect": {
                        "id":photo
                    }
                }
            },
            include={
                "photo":True,
            }
        )

        await prisma.disconnect()

        return user

    async def delete(self, id):
        await prisma.connect()

        user = await prisma.user.delete(
            where={
                'id': id
            }
        )

        await prisma.disconnect()

        return user

    async def verifyFollowing(self, follower: str, following: str) -> bool:
        await prisma.connect()

        values = await prisma.follows.find_first(
            where={
                "followerId": follower,
                "followingId": following
            }
        )

        await prisma.disconnect()

        return values is not None

    async def followUser(self, user_id: str, follow_id: str):
        await prisma.connect()

        values = await prisma.follows.create(
            data={
                "follower": {"connect": {"id": user_id}},
                "following": {"connect": {"id": follow_id}}
            }
        )

        await prisma.disconnect()
        return values

    async def deleteFollow(self, user_id: str, unfollow_id: str):
        await prisma.connect()

        await prisma.follows.delete(
            where={
                "followerId_followingId": {
                    "followerId": user_id,
                    "followingId": unfollow_id
                }
            }
        )

        await prisma.disconnect()

    async def findOther(self, id: str):
        await prisma.connect()

        users = await prisma.user.find_many(
            where={
                "id": {
                    "not": id
                }
            },
            order={
                'username': 'asc',
            },
            include={
                "barn": True,
                "followers":True,
                "following":True,
                "ownersDive":True,
                "photo":True,
                "reactions":True,
                "recipes":True,
                "usersDive":True
            }
        )

        await prisma.disconnect()

        return users
    
    async def searchUser(self,user_id:str,value:str):
        await prisma.connect()

        users = await prisma.user.find_many(
            where={
                "OR":[
                    {
                        "name":{
                            "contains":value
                        }
                    },
                    {
                        "username":{
                            "contains":value
                        }
                    }
                ],
                "NOT":{
                    "id":user_id
                }
            },
            include={
                "photo":True,
                "followers":True,
                "usersDive":True
            },
            order={
                "username":"asc"
            }
        )

        results = []

        for user in users:
            common_followers = 0
            common_dives = 0

            
            if user.followers is not None:
                common_followers = await prisma.follows.count(
                    where={
                        "followingId":user_id,
                        "followerId":user.id
                    }
                )
            
            if user.usersDive is not None:
                common_dives = await prisma.usersdive.count(
                    where={
                        "userId":user_id,
                        "diveId":{"in":[users_dive.diveId for users_dive in user.usersDive]}
                    }
                )

            result = {
                "user":user,
                "common_followers":common_followers,
                "common_dives": common_dives
            }

            results.append(result)


        await prisma.disconnect()

        return results