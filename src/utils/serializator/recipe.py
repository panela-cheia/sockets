import pytz

timezone = pytz.timezone('America/Sao_Paulo')

def recipeSerializator(recipe, reactions):
    recipe_formatted = {
        "id": recipe.id,
        "name": recipe.name,
        "description": recipe.description,
        "user": {
            "id": recipe.user.__dict__["id"],
            "name": recipe.user.__dict__["name"],
            "username": recipe.user.__dict__["username"],
            "photo": {
                "id": recipe.user.__dict__["photo"].id,
                "name": recipe.user.__dict__["photo"].name,
                "path": recipe.user.__dict__["photo"].path
            } if recipe.user.__dict__["photo"] else None
        },
        "photo": {
            "id": recipe.photo.__dict__["id"],
            "name": recipe.photo.__dict__["name"],
            "path": recipe.photo.__dict__["path"]
        } if recipe.photo.__dict__ else None,
        "ingredients": [ingredient.__dict__ for ingredient in recipe.ingredients],
        "reactions": {
            "bao": str(reactions["bão"]),
            "mio_de_bao": str(reactions["mió de bão"]),
            "agua_na_boca": str(reactions["água na boca"])
        },
        "created_at": recipe.created_at.astimezone(timezone).strftime("%d/%m/%Y")
    }

    return recipe_formatted