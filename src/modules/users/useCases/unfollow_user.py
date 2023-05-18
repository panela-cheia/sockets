import jwt
import json

from modules.users.repositories.user_repository import UserRepository


from shared.errors.errors import CustomError

class UnfollowUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, user_id: str, unfollow_id: str):
        # Verificar se o usuário existe
        user = await self.userRepository.findById(id=user_id)
        if not user:
            raise ValueError("User does not exist")

        # Verificar se o usuário está tentando deixar de seguir a si mesmo
        if user_id == unfollow_id:
            raise ValueError("Cannot unfollow yourself")

        # Verificar se o usuário a ser deixado de seguir existe
        unfollow_user = self.userRepository.findById(id=unfollow_id)
        if not unfollow_user:
            raise ValueError("User to unfollow does not exist")

        # Verificar se o usuário está seguindo o usuário a ser deixado de seguir
        existing_follow = self.userRepository.verifyFollowing(follower=user_id,following=unfollow_id)
        if not existing_follow:
            raise ValueError("Not following this user")


        return "Successfully unfollowed user"