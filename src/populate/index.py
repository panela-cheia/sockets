import asyncio
import os
import sys

# Adicione o diretório raiz do projeto ao caminho de pesquisa de módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# repositories
from modules.users.repositories.user_repository import UserRepository
from modules.files.repositories.files_repository import FilesRepository
from modules.recipes.repositories.recipe_repository import RecipeRepository
from modules.dive.repositories.dive_repository import DiveRepository
from modules.barn.repositories.barn_repository import BarnRepository

# usecases
from modules.users.useCases.create_user import CreateUserUseCase

from modules.files.useCases.create_file import CreateFileUseCase

from modules.recipes.useCases.create_recipe_usecase import CreateRecipeUseCase

from modules.dive.useCases.create_dive_usecase import CreateDiveUseCase

# dtos
from modules.users.dtos.create_user_dto import CreateUserDTO

from modules.files.dtos.create_file_dto import CreateFileDTO

from modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO
from modules.recipes.dtos.reactions_dto import ReactionDTO, ReactionType

from modules.dive.dtos.create_dive_dto import CreateDiveDTO

# utils
from utils.convert_list_convert_to_ingredient_dtos import convert_list_to_ingredient_dtos

createUserDTO = CreateUserDTO(
    name="Artur Papa",
    username="@moviepapa",
    email="artur.papa@ufv.br",
    password="12345678"
)

createUserDTO1 = CreateUserDTO(
    name="Luciano Belo",
    username="@luciano_belojr",
    email="luciano.alcantara@ufv.br",
    password="12345678"
)

createUserDTO2 = CreateUserDTO(
    name="Vinicius Mendes",
    username="@vinicmendes",
    email="vinicius.o.mendes@ufv.br",
    password="12345678"
)

createFileDTO = CreateFileDTO(
    name="file.png"
)

ingredient_data = [
    {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
    {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
    {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
]

userRepository = UserRepository()
filesRepository = FilesRepository()
recipeRepository = RecipeRepository()
diveRepository = DiveRepository()
barnRepository = BarnRepository()

createUserUseCase = CreateUserUseCase(userRepository=userRepository)

createFileUseCase = CreateFileUseCase(repository=filesRepository)

createRecipeUseCase = CreateRecipeUseCase(repository=recipeRepository)

createDiveUseCase = CreateDiveUseCase(repository=DiveRepository)
createDiveUseCase = CreateDiveUseCase(repository=diveRepository)

user = asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO))
asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO1))
asyncio.run(createUserUseCase.execute(createUserDTO=createUserDTO2))



file = asyncio.run(createFileUseCase.execute(createFileDTO=createFileDTO))

createRecipeDTO = CreateRecipeDTO(
    name="Receita",
    description="Nova Receita",
    ingredients=convert_list_to_ingredient_dtos(data=ingredient_data),
    userId=user.id,
    fileId=file.id
)

asyncio.run(createRecipeUseCase.execute(data=createRecipeDTO))


createDiveDTO = CreateDiveDTO(
    name="Buteco",
    description="Novo buteco",
    userId=user.id,
    fileId=file.id
)

asyncio.run(createDiveUseCase.execute(data=createDiveDTO))