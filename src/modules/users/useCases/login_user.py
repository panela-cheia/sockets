import jwt
import json

from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.create_user_dto import CreateUserDTO

from modules.users.providers.hash import compare

from shared.errors.errors import CustomError

from config.environments import MD5

class LoginUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, email,password):
        user = await self.userRepository.findByEmail(email)

        if not user:
            raise CustomError("User not exists")    

        if not compare(password,user.password):
            raise CustomError("Password does not match!")

        payload_data = {
            "sub": "4242",
            "id": user.id,
        }

        token = jwt.encode(
            payload=payload_data,
            key=MD5
        )

        # tirar b' do começo e ' do final

        response = {
            "user":{
                "id":user.id,
                "name":user.name,
                "username":user.username
            },
            "token":token
        }

        try:
           return response
        except:
            raise Exception("An error occurred during user creation")