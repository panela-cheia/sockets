from modules.users.repositories.user_repository import UserRepository
from modules.users.dtos.update_user_dto import UpdateUserDTO

from shared.errors.errors import CustomError

class UpdatePhotoUserUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self, id:str,photo: str):

        try:
            user = await self.userRepository.updatePhoto(
                id=id,
                photo=photo
            )
            return { "ok":"Successfully updated user: " + user["id"] }
        except:
            raise { "error": "An error occurred during user creation" }