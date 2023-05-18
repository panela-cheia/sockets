from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.update_user_dto import UpdateUserDTO

from shared.errors.errors import CustomError

class UpdateUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, id:str,updateUserDTO: UpdateUserDTO):

        verifyIfUsernameAlreadyBeenRegistered = await self.userRepository.findByUsername(updateUserDTO.username)

        if verifyIfUsernameAlreadyBeenRegistered:
            raise CustomError("This username has already been registered")

        # Verifica se o username começa com '@'
        if not updateUserDTO.username.startswith('@'):
            updateUserDTO.username = '@' + updateUserDTO.username

        try:
            user = await self.userRepository.update(
                id=id,
                bio=updateUserDTO.bio,
                name=updateUserDTO.name,
                username=updateUserDTO.username,
            )
            return user
        except:
            raise Exception("An error occurred during user creation")