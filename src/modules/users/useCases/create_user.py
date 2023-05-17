from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.create_user_dto import CreateUserDTO

from bcrypt import hashpw,gensalt

class CreateUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    def execute(self,createUserDTO:CreateUserDTO):
        passwordHash = hashpw(createUserDTO.password.encode("utf-8"),gensalt(rounds=8))
        
        try:
            user = self.userRepository.create(
                name=createUserDTO.name,
                username=createUserDTO.username,
                password=createUserDTO.password,
                email=createUserDTO.email
            )

            return user
        except:
            Exception("Erro!")
