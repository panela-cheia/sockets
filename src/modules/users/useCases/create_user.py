from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.create_user_dto import CreateUserDTO

from modules.users.providers.hash import hash

from shared.errors.errors import CustomError

class CreateUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, createUserDTO: CreateUserDTO):
        passwordHash = hash(createUserDTO.password)

        verifyIfEmailAlreadyBeenRegistered = await self.userRepository.findByEmail(createUserDTO.email)

        if verifyIfEmailAlreadyBeenRegistered:
            raise CustomError("This email has already been registered")        

        verifyIfUsernameAlreadyBeenRegistered = await self.userRepository.findByUsername(createUserDTO.username)

        if verifyIfUsernameAlreadyBeenRegistered:
            raise CustomError("This username has already been registered")

        # Verifica se o username começa com '@'
        if not createUserDTO.username.startswith('@'):
            createUserDTO.username = '@' + createUserDTO.username

        try:
            user = await self.userRepository.create(
                name=createUserDTO.name,
                username=createUserDTO.username,
                password=passwordHash,
                email=createUserDTO.email
            )
            return user
        except:
            raise Exception("An error occurred during user creation")