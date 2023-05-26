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
from modules.users.useCases.update_photo_user import UpdatePhotoUserUseCase
from modules.users.useCases.login_user import LoginUserUseCase
from modules.users.useCases.login_user_with_username import LoginUserWithUsernameUseCase
from modules.users.useCases.follow_user import FollowUserUseCase
from modules.users.useCases.unfollow_user import UnfollowUserUseCase
from modules.users.useCases.search_users import SearchUsersUseCase

from modules.files.useCases.create_file import CreateFileUseCase
from modules.files.useCases.delete_file import DeleteFileUseCase

from modules.recipes.useCases.create_recipe_usecase import CreateRecipeUseCase
from modules.recipes.useCases.list_usecase import ListRecipesUseCase
from modules.recipes.useCases.search_recipes_usecase import SearchRecipesUseCase
from modules.recipes.useCases.reaction_recipe_usecase import ReactionRecipeUseCase

from modules.barn.useCases.save_recipe import SaveRecipeUseCase
from modules.barn.useCases.search_recipe import SearhRecipeUseCase
from modules.barn.useCases.remove_recipe import RemoveRecipeUseCase

from modules.dive.useCases.create_dive_usecase import CreateDiveUseCase
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
from modules.dive.dtos.exit_dive_dto import ExitDiveDTO

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO

# utils
from utils.convert_list_convert_to_ingredient_dtos import convert_list_to_ingredient_dtos


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
        listOthersUseCase = ListOthersUseCase(userRepository=userRepository)
        followUserUseCase= FollowUserUseCase(userRepository=userRepository)
        unfollowUserUseCase= UnfollowUserUseCase(userRepository=userRepository)
        updateUserUseCase= UpdateUserUseCase(userRepository=userRepository)
        updatePhotoUserUseCase = UpdatePhotoUserUseCase(userRepository=userRepository)
        searchUsersUseCase = SearchUsersUseCase(userRepository=userRepository)

        createFileUseCase = CreateFileUseCase(repository=filesRepository)
        deleteFileUseCase = DeleteFileUseCase(repository=filesRepository)

        createRecipeUseCase = CreateRecipeUseCase(repository=recipeRepository)
        listRecipesUseCase = ListRecipesUseCase(repository=recipeRepository)
        searchRecipesUseCase = SearchRecipesUseCase(repository=recipeRepository)
        reactionRecipeUseCase = ReactionRecipeUseCase(repository=recipeRepository)

        saveRecipeInBarnUseCase = SaveRecipeUseCase(repository=barnRepository)
        searchRecipeUseCase = SearhRecipeUseCase(repository=barnRepository)
        removeRecipeUseCase = RemoveRecipeUseCase(repository=barnRepository)

        createDiveUseCase = CreateDiveUseCase(repository=DiveRepository)
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
            users = await listOthersUseCase.execute(id=body["id"])
            logger.info("{topic} - {users}",topic=Topics.USER_LIST_OTHERS.value,users=users)

        elif topic == Topics.USER_FOLLOW.value:
            follow = await followUserUseCase.execute(user_id=body["user_id"],follow_id=body["follow_id"])
            logger.info("{topic} - {response}",topic=Topics.USER_FOLLOW.value,response=follow)

        elif topic == Topics.USER_UNFOLLOW.value:
            unfollow = await unfollowUserUseCase.execute(user_id=body["user_id"],unfollow_id=body["unfollow_id"])
            logger.info("{topic} - {response}",topic=Topics.USER_UNFOLLOW.value,response=unfollow)

        elif topic == Topics.USER_UPDATE.value:
            updateUserDTO = UpdateUserDTO(
                bio=body["bio"],
                name=body["name"],
                username=body["username"]
            )

            update = await updateUserUseCase.execute(id=body["id"],updateUserDTO=updateUserDTO)
            logger.info("{topic} - {response}",topic=Topics.USER_UPDATE.value,response=update)

        elif topic == Topics.USER_UPDATE_PHOTO.value:
            update = await updatePhotoUserUseCase.execute(id=body["id"],photo=body["photo"])
            logger.info("{topic} - {response}",topic=Topics.USER_UPDATE_PHOTO.value,response=update)
        
        elif topic == Topics.USER_SEARCH_USERS.value:
            users = await searchUsersUseCase.execute(user_id=body["user_id"],value=body["value"])
            logger.info("{topic} - {response}",topic=Topics.USER_SEARCH_USERS.value,response=json.dumps(users,indent=4,ensure_ascii=False))

        elif topic == Topics.BARN_SEARCH_RECIPE.value:
            dto = SearchRecipeInBarnDTO(barnId=body["id"],recipeName=body["name"])
            recipes = await searchRecipeUseCase.execute(data=dto)
            logger.info("{topic} - {response}",topic=Topics.BARN_SEARCH_RECIPE.value,response=recipes)

        elif topic == Topics.BARN_SAVE_RECIPE.value:
            dto = BarnSaveRecipeDTO(barnId=body["id"],recipeId=body["recipe_id"])
            barn = await saveRecipeInBarnUseCase.execute(data=dto)
            logger.info("{topic} - {response}",topic=Topics.BARN_SAVE_RECIPE.value,response=barn)

        elif topic == Topics.BARN_REMOVE_RECIPE.value:
            dto = RemoveRecipeDTO(barnId=body["id"],recipeId=body["recipe_id"])
            barn = await removeRecipeUseCase.execute(data=dto)
            logger.info("{topic} - {response}",topic=Topics.BARN_REMOVE_RECIPE.value,response=barn)

        elif topic == Topics.FILE_CREATE.value:
            createFileDTO = CreateFileDTO(name=body["name"])
            file = await createFileUseCase.execute(createFileDTO=createFileDTO)
            logger.info("{topic} - {response}",topic=Topics.FILE_CREATE.value,response=file)

        elif topic == Topics.FILE_DELETE.value:
            deleteFileDTO = DeleteFileDTO(id=body["id"])
            file = await deleteFileUseCase.execute(deleteFileDTO=deleteFileDTO)
            logger.info("{topic} - {response}",topic=Topics.FILE_DELETE.value,response=file)
        
        elif topic == Topics.RECIPE_CREATE.value:
            createRecipeDTO = CreateRecipeDTO(
                name=body["name"],
                description=body["description"],
                ingredients=convert_list_to_ingredient_dtos(data=body["ingredients"]),
                userId=body["userId"],
                fileId=body["fileId"]
            )

            recipe = await createRecipeUseCase.execute(data=createRecipeDTO)
            logger.info("{topic} - {response}",topic=Topics.RECIPE_CREATE.value,response=recipe)

        elif topic == Topics.RECIPE_LIST.value:
            recipes = await listRecipesUseCase.execute()
            logger.info("{topic} - {response}",topic=Topics.RECIPE_LIST.value,response=json.dumps(recipes,indent=4,ensure_ascii=False))

        elif topic == Topics.RECIPE_REACTION.value:
            type = ReactionType(body["type"])
            dto = ReactionDTO(type=type.value,recipe_id=body["recipe_id"],user_id=body["user_id"])
            reaction = await reactionRecipeUseCase.execute(reaction_data=dto) 
            logger.info("{topic} - {response}",topic=Topics.RECIPE_REACTION.value,response=reaction)

        elif topic == Topics.RECIPE_SEARCH.value:
            recipes = await searchRecipesUseCase.execute(name=body["name"])
            logger.info("{topic} - {response}",topic=Topics.RECIPE_SEARCH.value,response=recipes)

        elif topic == Topics.DIVE_CREATE.value:
            createDiveDTO = CreateDiveDTO(
                name=body["name"],
                description=body["description"],
                fileId=body["fileId"],
                userId=body["userId"]
            )

            dive = await createDiveUseCase.execute(data=createDiveDTO)
            logger.info("{topic} - {response}",topic=Topics.DIVE_CREATE.value,response=dive)
        
        elif topic == Topics.DIVE_SEARCH.value:
            dive = await searchDiveUseCase.execute(diveName=body["name"])
            logger.info("{topic} - {response}",topic=Topics.DIVE_SEARCH.value,response=dive)

        elif topic == Topics.DIVE_ENTER.value:
            dive = await enterDiveUseCase.execute(user_id=body["id"],dive_id=body["diveId"])
            logger.info("{topic} - {response}",topic=Topics.DIVE_ENTER.value,response=dive)
        
        elif topic == Topics.DIVE_EXIT.value:
            exitDiveDTO = ExitDiveDTO(
                user=body["user"],
                new_owner=body["new_owner"],
                diveId=body["diveId"]
            )
            
            dive = await exitDiveUseCase.execute(data=exitDiveDTO)
            logger.info("{topic} - {response}",topic=Topics.DIVE_EXIT.value,response=dive)

        elif topic == Topics.DIVE_UPDATE.value:
            print(Topics.DIVE_UPDATE.value)