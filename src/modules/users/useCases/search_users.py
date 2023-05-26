from modules.users.repositories.user_repository import UserRepository
from utils.serializator.search_uses import searchUsersSerializator

class SearchUsersUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self,user_id:str,value:str):
        users = await self.userRepository.searchUser(user_id=user_id,value=value)

        results = [ ]

        for user in users:
            results.append(searchUsersSerializator(user))

        return results