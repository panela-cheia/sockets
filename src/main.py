import asyncio
from modules.users.repositories.user_repository import UserRepository
from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.useCases.list_all_users import ListAllUsersUseCase
from modules.users.dtos.create_user_dto import CreateUserDTO

if __name__ == "__main__":
    userRepository = UserRepository()
    
    createUserUseCase = CreateUserUseCase(userRepository=userRepository)
    listAllUsersUseCase= ListAllUsersUseCase(userRepository=userRepository)

    createUserDTO = CreateUserDTO(
        name="testes-4",
        username="@teste-4",
        email="teste-4.teste@ufv.br",
        password="12345678"
    )
   
    # user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
    users = asyncio.run(listAllUsersUseCase.execute())
    # print(user)
    print(users)