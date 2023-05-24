import json
from constants.topics import Topics
from loguru import logger

# Configuração básica do logger
logger.add("app.log", rotation="500 MB", retention="10 days", level="INFO")

# repositories
from modules.users.repositories.user_repository import UserRepository
from modules.files.repositories.files_repository import FilesRepository
from modules.recipes.repositories.recipe_repository import RecipeRepository
from modules.dive.repositories.dive_repository import DiveRepository
from modules.barn.repositories.barn_repository import BarnRepository

# usecases
from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.useCases.list_all_users import ListAllUsersUseCase
from modules.users.useCases.list_others import ListOthersUseCase
from modules.users.useCases.update_user import UpdateUserUseCase
from modules.users.useCases.login_user import LoginUserUseCase
from modules.users.useCases.login_user_with_username import LoginUserWithUsernameUseCase
from modules.users.useCases.follow_user import FollowUserUseCase
from modules.users.useCases.unfollow_user import UnfollowUserUseCase

from modules.files.useCases.create_file import CreateFileUseCase
from modules.files.useCases.delete_file import DeleteFileUseCase

from modules.recipes.useCases.create_recipe_usecase import CreateRecipeUseCase
from modules.recipes.useCases.list_usecase import ListRecipesUseCase
from modules.recipes.useCases.search_recipes_usecase import SearchRecipesUseCase
from modules.recipes.useCases.reaction_recipe_usecase import ReactionRecipeUseCase

from modules.dive.useCases.create_dive_usecase import CreateDiveUseCase
from modules.barn.useCases.save_recipe import SaveRecipeUseCase
from modules.barn.useCases.search_recipe import SearhRecipeUseCase
from modules.barn.useCases.remove_recipe import RemoveRecipeUseCase
from modules.dive.useCases.enter_dive import EnterDiveUseCase
from modules.dive.useCases.exit_dive import ExitDiveUseCase
from modules.dive.useCases.update_dive import UpdateDiveUseCase
from modules.dive.useCases.search_dive import SearchDiveUseCase

# dtos
from modules.users.dtos.create_user_dto import CreateUserDTO
from modules.users.dtos.update_user_dto import UpdateUserDTO

from modules.files.dtos.create_file_dto import CreateFileDTO
from modules.files.dtos.delete_file_dto import DeleteFileDTO

from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO
from modules.recipes.dtos.reactions_dto import ReactionDTO,ReactionType

from modules.dive.dtos.create_dive_dto import CreateDiveDTO
from modules.dive.dtos.update_dive_dto import UpdateDiveDTO

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO

class Bootstrap:
    def __init__(self)-> None:
        pass

    async def run(self,message:str):
        userRepository = UserRepository()
        filesRepository = FilesRepository()
        recipeRepository = RecipeRepository()
        diveRepository = DiveRepository()
        barnRepository = BarnRepository()

        createUserUseCase = CreateUserUseCase(userRepository=userRepository)
        loginUserUseCase= LoginUserUseCase(userRepository=userRepository)
        loginUserWithUsernameUseCase= LoginUserWithUsernameUseCase(userRepository=userRepository)
        listAllUsersUseCase = ListAllUsersUseCase(userRepository=userRepository)
        followUserUseCase= FollowUserUseCase(userRepository=userRepository)
        unfollowUserUseCase= UnfollowUserUseCase(userRepository=userRepository)
        updateUserUseCase= UpdateUserUseCase(userRepository=userRepository)

        createFileUseCase = CreateFileUseCase(repository=filesRepository)
        deleteFileUseCase = DeleteFileUseCase(repository=filesRepository)

        createRecipeUseCase = CreateRecipeUseCase(repository=recipeRepository)
        listRecipesUseCase = ListRecipesUseCase(repository=recipeRepository)
        searchRecipesUseCase = SearchRecipesUseCase(repository=recipeRepository)
        reactionRecipeUseCase = ReactionRecipeUseCase(repository=recipeRepository)

        createDiveUseCase = CreateDiveUseCase(repository=DiveRepository)
        saveRecipeInBarnUseCase = SaveRecipeUseCase(repository=barnRepository)
        searchRecipesUseCase = SearhRecipeUseCase(repository=barnRepository)
        removeRecipeUseCase = RemoveRecipeUseCase(repository=barnRepository)
        createDiveUseCase = CreateDiveUseCase(repository=diveRepository)
        enterDiveUseCase = EnterDiveUseCase(repository=diveRepository)
        exitDiveUseCase = ExitDiveUseCase(repository=diveRepository)
        updateDiveUseCase = UpdateDiveUseCase(repository=diveRepository)
        searchDiveUseCase = SearchDiveUseCase(repository=diveRepository)

        content = json.loads(message)

        try:
            topic = Topics(content["topic"])
            body = content["body"]
        except (KeyError, ValueError):
            logger.critical("Invalid message format")

        if topic == Topics.USER_CREATE.value:
            createUserDTO = CreateUserDTO(
                name=body["name"],
                username=body["username"],
                email=body["email"],
                password=body["password"]
            )

            try:
                user = await createUserUseCase.execute(createUserDTO=createUserDTO)
                logger.info("{topic} - {user}",topic=Topics.USER_CREATE.value,user=user)

            except (ValueError):
                raise Exception(ValueError)

        elif topic == Topics.USER_LOGIN_EMAIL.value:
            user = await loginUserUseCase.execute(email=body["email"],password=body["password"])
            logger.info("{topic} - {user}",topic=Topics.USER_LOGIN_EMAIL.value,user=user)

        elif topic == Topics.USER_LOGIN_USERNAME.value:
            user = await loginUserWithUsernameUseCase.execute(username=body["username"],password=body["password"])
            logger.info("{topic} - {user}",topic=Topics.USER_LOGIN_USERNAME.value,user=user)

        elif topic == Topics.USER_LIST.value:
            users = await listAllUsersUseCase.execute()
            logger.info("{topic} - {users}",topic=Topics.USER_LIST.value,users=users)

        elif topic == Topics.USER_LIST_OTHERS.value:
            print(Topics.USER_LIST_OTHERS.value)

        elif topic == Topics.USER_FOLLOW.value:
            print(Topics.USER_FOLLOW.value)

        elif topic == Topics.USER_UNFOLLOW.value:
            print(Topics.USER_UNFOLLOW.value)

        elif topic == Topics.USER_UPDATE.value:
            print(Topics.USER_UPDATE.value)

        elif topic == Topics.USER_UPDATE_PHOTO.value:
            print(Topics.USER_UPDATE_PHOTO.value)

        elif topic == Topics.BARN_SEARCH_RECIPE.value:
            print(Topics.BARN_SEARCH_RECIPE.value)

        elif topic == Topics.BARN_SAVE_RECIPE.value:
            print(Topics.BARN_SAVE_RECIPE.value)

        elif topic == Topics.BARN_REMOVE_RECIPE.value:
            print(Topics.BARN_REMOVE_RECIPE.value)

        elif topic == Topics.FILE_CREATE.value:
            print(Topics.FILE_CREATE.value)

        elif topic == Topics.FILE_DELETE.value:
            print(Topics.FILE_DELETE.value)
        
        elif topic == Topics.RECIPE_CREATE.value:
            print(Topics.RECIPE_CREATE.value)

        elif topic == Topics.RECIPE_LIST.value:
            print(Topics.RECIPE_LIST.value)

        elif topic == Topics.RECIPE_REACTION.value:
            print(Topics.RECIPE_REACTION.value)

        elif topic == Topics.RECIPE_SEARCH.value:
            print(Topics.RECIPE_SEARCH.value)

        elif topic == Topics.DIVE_CREATE.value:
            print(Topics.DIVE_CREATE.value)
        
        elif topic == Topics.DIVE_SEARCH.value:
            print(Topics.DIVE_SEARCH.value)

        elif topic == Topics.DIVE_ENTER.value:
            print(Topics.DIVE_ENTER.value)
        
        elif topic == Topics.DIVE_EXIT.value:
            print(Topics.DIVE_EXIT.value)

        elif topic == Topics.DIVE_UPDATE.value:
            print(Topics.DIVE_UPDATE.value)