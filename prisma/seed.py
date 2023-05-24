import asyncio
import sys
import os

from typing import List

from prisma import Prisma

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# dtos
from src.modules.users.dtos.create_user_dto import CreateUserDTO

from src.modules.files.dtos.create_file_dto import CreateFileDTO

from src.modules.recipes.dtos.create_recipe_dto import CreateRecipeDTO,IngredientDTO

from src.modules.dive.dtos.create_dive_dto import CreateDiveDTO

# providers
from src.providers.hash import hash

# config
from src.config.app_url import APP_URL

async def seed():
    prisma = Prisma()

    createUserDTO = CreateUserDTO(
        name="Artur Papa",
        username="@moviepapa",
        email="artur.papa@ufv.br",
        password=hash("12345678",8)
    )

    createUserDTO1 = CreateUserDTO(
        name="Luciano Belo",
        username="@luciano_belojr",
        email="luciano.alcantara@ufv.br",
        password=hash("12345678",8)
    )

    createUserDTO2 = CreateUserDTO(
        name="Vinicius Mendes",
        username="@vinicmendes",
        email="vinicius.o.mendes@ufv.br",
        password=hash("12345678",8)
    )

    createFileDTO = CreateFileDTO(
        name="file.png"
    )

    ingredient_data = [
        {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
        {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
        {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
    ]

    try:
        await prisma.connect()

        user = await prisma.user.create(
            data={
                "name": createUserDTO.name,
                "username": createUserDTO.username,
                "email": createUserDTO.email,
                "password": createUserDTO.password
            }
        )

        await prisma.barn.create(
            data={
                "user": {
                    "connect": {
                        "id": user.id
                    }
                }
            }
        )

        user1 = await prisma.user.create(
            data={
                "name": createUserDTO1.name,
                "username": createUserDTO1.username,
                "email": createUserDTO1.email,
                "password": createUserDTO1.password
            }
        )

        await prisma.barn.create(
            data={
                "user": {
                    "connect": {
                        "id": user1.id
                    }
                }
            }
        )

        user2 = await prisma.user.create(
            data={
                "name": createUserDTO2.name,
                "username": createUserDTO2.username,
                "email": createUserDTO2.email,
                "password": createUserDTO2.password
            }
        )

        await prisma.barn.create(
            data={
                "user": {
                    "connect": {
                        "id": user2.id
                    }
                }
            }
        )

        # create file
        extension = createFileDTO.name[-4:]

        path = APP_URL + "/statics/" + createFileDTO.name

        if extension != ".png" and extension != ".jpg":
            raise Exception("Extension is not permitted!")
        
        nameHashed = hash(value=createFileDTO.name,gensalt=4)

        finalName = nameHashed +  "-" + createFileDTO.name

        fileCreated = await prisma.file.create(data={
            "name":finalName,
            "path":path
        })

        # create recipe
        createRecipeDTO = CreateRecipeDTO(
            name="Receita",
            description="Nova Receita",
            ingredients=convert_list_to_ingredient_dtos(data=ingredient_data),
            userId=user.id,
            fileId=fileCreated.id
        )

        await prisma.recipe.create(data={
            "name": createRecipeDTO.name,
            "description": createRecipeDTO.description,
            "userId": createRecipeDTO.userId,
            "diveId": createRecipeDTO.diveId,
            "fileId": createRecipeDTO.fileId,
            "ingredients": {
                "create": [
                    {
                        "name": ingredient.name,
                        "amount": ingredient.amount,
                        "unit": ingredient.unit

                    }
                    for ingredient in createRecipeDTO.ingredients
                ]
            }   
        })

        # create dive

        createDiveDTO = CreateDiveDTO(
            name="Buteco",
            description="Novo buteco",
            userId=user.id,
            fileId=fileCreated.id
        )

        await prisma.dive.create(data={
            "name":createDiveDTO.name,
            "description":createDiveDTO.description,
            "fileId":createDiveDTO.fileId,
            "userId":createDiveDTO.userId
        })

        await prisma.disconnect()
    except:
        raise Exception("Error to try run seed!")


def convert_list_to_ingredient_dtos(data: List[dict]) -> List[IngredientDTO]:
    ingredient_dtos = []
    for item in data:
        ingredient_dto = IngredientDTO(name=item['name'], amount=item['amount'], unit=item['unit'])
        ingredient_dtos.append(ingredient_dto)
    return ingredient_dtos


asyncio.run(seed())