from modules.users.repositories.user_repository import UserRepository
from utils.serializator.user_profile import userProfileSerializator

class UserProfileUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self,user_id:str):
        user = await self.userRepository.findById(id=user_id)

        if not user:
            raise ValueError("User does not exist")

        return userProfileSerializator(user=user)