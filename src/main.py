import asyncio
import sys

# repositories
from modules.users.repositories.user_repository import UserRepository
from modules.files.repositories.files_repository import FilesRepository
from modules.recipes.repositories.recipe_repository import RecipeRepository
from modules.barn.repositories.barn_repository import BarnRepository

# usecases
from modules.users.useCases.create_user import CreateUserUseCase
from modules.users.useCases.list_all_users import ListAllUsersUseCase
from modules.users.useCases.update_user import UpdateUserUseCase
from modules.users.useCases.login_user import LoginUserUseCase
from modules.users.useCases.login_user_with_username import LoginUserWithUsernameUseCase
from modules.users.useCases.follow_user import FollowUserUseCase
from modules.users.useCases.unfollow_user import UnfollowUserUseCase
from modules.users.useCases.list_others import ListOthersUseCase

from modules.files.useCases.create_file import CreateFileUseCase
from modules.files.useCases.delete_file import DeleteFileUseCase

from modules.recipes.useCases.create_recipe_usecase import CreateRecipeUseCase
from modules.recipes.useCases.list_usecase import ListRecipesUseCase
from modules.recipes.useCases.serch_recipes_usecase import SearchRecipesUseCase
from modules.recipes.useCases.reaction_recipe_usecase import ReactionRecipeUseCase

from modules.barn.useCases.save_recipe import SaveRecipeUseCase
from modules.barn.useCases.sarch_recipe import SearhRecipeUseCase
from modules.barn.useCases.remove_recipe import RemoveRecipeUseCase

# dtos
from modules.users.dtos.create_user_dto import CreateUserDTO
from modules.users.dtos.update_user_dto import UpdateUserDTO

from modules.files.dtos.create_file_dto import CreateFileDTO
from modules.files.dtos.delete_file_dto import DeleteFileDTO

from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO
from modules.recipes.dtos.reactions_dto import ReactionDTO,ReactionType

from modules.barn.dtos.save_recipe_dto import BarnSaveRecipeDTO
from modules.barn.dtos.search_recipe_in_barn_dto import SearchRecipeInBarnDTO
from modules.barn.dtos.remove_recipe_dto import RemoveRecipeDTO

#utils
from utils.convert_list_convert_to_ingredient_dtos import convert_list_to_ingredient_dtos

# sys.tracebacklimit=0

if __name__ == "__main__":
    userRepository = UserRepository()
    filesRepository = FilesRepository()
    recipeRepository = RecipeRepository()
    barnRepository = BarnRepository()
    
    createUserUseCase = CreateUserUseCase(userRepository=userRepository)
    listAllUsersUseCase= ListAllUsersUseCase(userRepository=userRepository)
    listOthersUseCase= ListOthersUseCase(userRepository=userRepository)
    updateUserUseCase= UpdateUserUseCase(userRepository=userRepository)
    loginUserUseCase= LoginUserUseCase(userRepository=userRepository)
    loginUserWithUsernameUseCase= LoginUserWithUsernameUseCase(userRepository=userRepository)
    followUserUseCase= FollowUserUseCase(userRepository=userRepository)
    unfollowUserUseCase= UnfollowUserUseCase(userRepository=userRepository)

    createFileUseCase = CreateFileUseCase(repository=filesRepository)
    deleteFileUseCase = DeleteFileUseCase(repository=filesRepository)

    createRecipeUseCase = CreateRecipeUseCase(repository=recipeRepository)
    listRecipesUseCase = ListRecipesUseCase(repository=recipeRepository)
    searchRecipesUseCase = SearchRecipesUseCase(repository=recipeRepository)
    reactionRecipeUseCase = ReactionRecipeUseCase(repository=recipeRepository)

    saveRecipeInBarnUseCase = SaveRecipeUseCase(repository=barnRepository)
    searchRecipesUseCase = SearhRecipeUseCase(repository=barnRepository)
    removeRecipeUseCase = RemoveRecipeUseCase(repository=barnRepository)

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

    deleteFileDTO = DeleteFileDTO(
        id="c1a13582-9997-4c24-8a7e-fd3e40fd5e63"
    )

    ingredient_data = [
        {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
        {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
        {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
    ]
   
    createRecipeDTO = CreateRecipeDTO(
        name="Teste",
        description="new recipe",
        ingredients=convert_list_to_ingredient_dtos(data=ingredient_data),
        userId="3bb76893-2547-435f-a209-5d294726c5af",
        fileId="c1a13582-9997-4c24-8a7e-fd3e40fd5e63"
    )

    saveRecipeInBarnDTO = BarnSaveRecipeDTO(
        barnId="804e869c-3c2b-4776-884e-669e57e2c204",
        recipeId="f1158dc9-9d6e-4940-b215-167076752a2c"
    )

    removeRecipeDTO = RemoveRecipeDTO(
        barnId="804e869c-3c2b-4776-884e-669e57e2c204",
        recipeId="f1158dc9-9d6e-4940-b215-167076752a2c"
    )

    searchRecipesDTO = SearchRecipeInBarnDTO(barnId="804e869c-3c2b-4776-884e-669e57e2c204", recipeName="Teste")

    # type = ReactionType.MIO_DE_BAO
    # print(type)

    # reactionDTO = ReactionDTO(type=type.value,recipe_id="468caf9d-fc04-440a-8395-44542f76f2dc",user_id="3bb76893-2547-435f-a209-5d294726c5af")

    # user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
    # users = asyncio.run(updateUserUseCase.execute(id="3bb76893-2547-435f-a209-5d294726c5af",updateUserDTO=updateUserDTO))
    # print(user)
    
    # value = asyncio.run(loginUserUseCase.execute(createUserDTO.email,"12345678"))
    # users = asyncio.run(listAllUsersUseCase.execute())

    # fileCreated = asyncio.run(createFileUseCase.execute(createFileDTO))
    # fileDeleted = asyncio.run(deleteFileUseCase.execute(deleteFileDTO))

    # users = asyncio.run(listOthersUseCase.execute("3bb76893-2547-435f-a209-5d294726c5af"))

    # recipe = asyncio.run(createRecipeUseCase.execute(data=createRecipeDTO))
    # recipes = asyncio.run(listRecipesUseCase.execute())
    # recipes = asyncio.run(searchRecipesUseCase.execute(name="test"))
    # recipes = asyncio.run(reactionRecipeUseCase.execute(reaction_data=reactionDTO))

    # barn = asyncio.run(saveRecipeInBarnUseCase.execute(data=saveRecipeInBarnDTO))
    # recipesInBarn = asyncio.run(searchRecipesUseCase.execute(data=searchRecipesDTO))
    removeRecipe = asyncio.run(removeRecipeUseCase.execute(data=removeRecipeDTO))

    print(removeRecipe)

    # print(users)