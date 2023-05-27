from modules.dive.repositories.dive_repository import DiveRepository
from modules.users.repositories.user_repository import UserRepository

from modules.search.dtos.search_dive_and_users_dto import SearchDiveAndUserDTO

from utils.serializator.list_dive import listDiveSerializator
from utils.serializator.search_uses import searchUsersSerializator

class SearchDiveAndUserUseCase:
    def __init__(self, diveRepository: DiveRepository,userRepository:UserRepository):
        self.diveRepository = diveRepository
        self.userRepository = userRepository

    async def execute(self, data: SearchDiveAndUserDTO):
        dives =  await self.diveRepository.findAll(name=data.search_value)

        all_dives = []

        for dive in dives:
            dive_formatted = listDiveSerializator(dive=dive)
            all_dives.append(dive_formatted)

        users = await self.userRepository.searchUser(user_id=data.user_id,value=data.search_value)

        all_users = [ ]

        for user in users:
            all_users.append(searchUsersSerializator(user))

        data = {
            "dives": all_dives,
            "users": all_users
        }

        return data