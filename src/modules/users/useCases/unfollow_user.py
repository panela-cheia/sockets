import jwt
import json

from modules.users.repositories.user_repository import UserRepository


from shared.errors.errors import CustomError

class UnfollowUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, user_id: str, unfollow_id: str):
        # Verificar se o usuário existe
        user = await self.userRepository.findById(user_id)
        unfollow_user = await self.userRepository.findById(unfollow_id)

        if not user:
            raise ValueError("Invalid user ID")

        if not unfollow_user:
            raise ValueError("Invalid unfollow user ID")

        # Verificar se o usuário está seguindo o usuário a ser deixado de seguir
        existing_follow = await self.userRepository.verifyFollowing(follower=user_id,following=unfollow_id)
        if not existing_follow:
            raise ValueError("Not following this user")
        
        await self.userRepository.deleteFollow(user_id=user_id,unfollow_id=unfollow_id)

        return "Successfully unfollowed user"