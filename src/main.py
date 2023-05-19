import asyncio
import sys

from modules.users.repositories.user_repository import UserRepository
from modules.files.repositories.files_repository import FilesRepository

from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.useCases.list_all_users import ListAllUsersUseCase
from modules.users.useCases.update_user import UpdateUserUseCase
from modules.users.useCases.login_user import LoginUserUseCase
from modules.users.useCases.login_user_with_username import LoginUserWithUsernameUseCase
from modules.users.useCases.follow_user import FollowUserUseCase
from modules.users.useCases.unfollow_user import UnfollowUserUseCase
from modules.users.useCases.list_others import ListOthersUseCase

from modules.files.useCases.create_file import CreateFileUseCase

from modules.users.dtos.create_user_dto import CreateUserDTO
from modules.users.dtos.update_user_dto import UpdateUserDTO

from modules.files.dtos.create_file_dto import CreateFileDTO

sys.tracebacklimit=0

if __name__ == "__main__":
    userRepository = UserRepository()
    filesRepository = FilesRepository()
    
    createUserUseCase = CreateUserUseCase(userRepository=userRepository)
    listAllUsersUseCase= ListAllUsersUseCase(userRepository=userRepository)
    listOthersUseCase= ListOthersUseCase(userRepository=userRepository)
    updateUserUseCase= UpdateUserUseCase(userRepository=userRepository)
    loginUserUseCase= LoginUserUseCase(userRepository=userRepository)
    loginUserWithUsernameUseCase= LoginUserWithUsernameUseCase(userRepository=userRepository)
    followUserUseCase= FollowUserUseCase(userRepository=userRepository)
    unfollowUserUseCase= UnfollowUserUseCase(userRepository=userRepository)

    createFileUseCase = CreateFileUseCase(repository=filesRepository)

    createUserDTO = CreateUserDTO(
        name="Vinicius Mendes",
        username="@vinicsmendes",
        email="vinicius.mendes@ufv.br",
        password="12345678"
    )

    updateUserDTO = UpdateUserDTO(
        bio="ex de amigo é igual cebola...",
        name="Artur Papa",
        username="@papaart",
    )

    createFileDTO = CreateFileDTO(
        name="file.png"
    )
   
    # user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
    # users = asyncio.run(updateUserUseCase.execute(id="3bb76893-2547-435f-a209-5d294726c5af",updateUserDTO=updateUserDTO))
    # print(user)
    
    # value = asyncio.run(loginUserUseCase.execute(createUserDTO.email,"12345678"))
    # users = asyncio.run(listAllUsersUseCase.execute())

    # fileCreated = asyncio.run(createFileUseCase.execute(createFileDTO))

    users = asyncio.run(listOthersUseCase.execute("3bb76893-2547-435f-a209-5d294726c5af"))
 
    print(users)

    # print(users)