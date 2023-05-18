import asyncio
import sys

from modules.users.repositories.user_repository import UserRepository

from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.useCases.list_all_users import ListAllUsersUseCase
from modules.users.useCases.update_user import UpdateUserUseCase
from modules.users.useCases.login_user import LoginUserUseCase
from modules.users.useCases.follow_user import FollowUserUseCase
from modules.users.useCases.unfollow_user import UnfollowUserUseCase

from modules.users.dtos.create_user_dto import CreateUserDTO
from modules.users.dtos.update_user_dto import UpdateUserDTO

# sys.tracebacklimit=0

if __name__ == "__main__":
    userRepository = UserRepository()
    
    createUserUseCase = CreateUserUseCase(userRepository=userRepository)
    listAllUsersUseCase= ListAllUsersUseCase(userRepository=userRepository)
    updateUserUseCase= UpdateUserUseCase(userRepository=userRepository)
    loginUserUseCase= LoginUserUseCase(userRepository=userRepository)
    followUserUseCase= FollowUserUseCase(userRepository=userRepository)
    unfollowUserUseCase= UnfollowUserUseCase(userRepository=userRepository)

    createUserDTO = CreateUserDTO(
        name="testes-8",
        username="@teste-8",
        email="teste-8.teste@ufv.br",
        password="12345678"
    )

    updateUserDTO = UpdateUserDTO(
        bio="comida é vida!",
        name="Luciano",
        username="@lucianobajr",
    )
   
    # user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
    # users = asyncio.run(updateUserUseCase.execute(id="8953bfff-06f5-4f7b-b5bd-7bf88a57f114",updateUserDTO=updateUserDTO))
    # print(user)
    
    # value = asyncio.run(loginUserUseCase.execute(createUserDTO.email,"12345678"))
    users = asyncio.run(listAllUsersUseCase.execute())

    
    follow = asyncio.run(unfollowUserUseCase.execute(
        user_id="0ceeaf5c-2a0d-4867-a415-c600276ed5f9",
        unfollow_id="bf5f0683-16dd-4123-960d-48cb84321db5"
    ))

    print(follow)
    print(users)