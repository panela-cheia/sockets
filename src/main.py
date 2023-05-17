import asyncio
from modules.users.repositories.user_repository import UserRepository
from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.dtos.create_user_dto import CreateUserDTO

if __name__ == "__main__":
    userRepository = UserRepository()
    createUserUseCase = CreateUserUseCase(userRepository=userRepository)

    createUserDTO = CreateUserDTO(
        name="vinicius",
        username="@vinicmendes",
        email="vinicius.mendes@ufv.br",
        password="12345678"
    )

    user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
    # users = asyncio.run(userRepository.findAll())
         
    print(user)