import jwt
import json

from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.create_user_dto import CreateUserDTO

from providers.hash import compare

from shared.errors.errors import CustomError

from config.environments import MD5

class LoginUserWithUsernameUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, username,password):
        user = await self.userRepository.findByUsername(username)

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

        response = {
            "user":{
                "id":user.id,
                "name":user.name,
                "username":user.username,
                "email":user.email
            },
            "token":token.decode('utf-8')
        }

        response_json = json.dumps(response)

        try:
           return response_json
        except:
            raise Exception("An error occurred during user creation")