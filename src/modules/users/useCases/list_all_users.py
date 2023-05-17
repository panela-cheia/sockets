from modules.users.repositories.user_repository import UserRepository
    
class ListAllUsersUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self):
        users = await self.userRepository.findAll()

        return users