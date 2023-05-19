from modules.users.repositories.user_repository import UserRepository

class ListOthersUseCase:
    def __init__(self,userRepository:UserRepository) -> None:
        self.userRepository = userRepository

    async def execute(self,id:str):
        verifyIfUserExists = await self.userRepository.findById(id)

        if not verifyIfUserExists:
            raise ValueError("Invalid user ID")
        
        return await self.userRepository.findOther(id)