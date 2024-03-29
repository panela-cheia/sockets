import pytz

timezone = pytz.timezone('America/Sao_Paulo')

def recipeWithoutReactionsSerializator(recipe):
    recipe_formatted = {
        "id": recipe.id,
        "name": recipe.name,
        "description": recipe.description,
        "photo": {
            "id": recipe.photo.__dict__["id"] ,
            "name": recipe.photo.__dict__["name"],
            "path": recipe.photo.__dict__["path"]
        } if recipe.photo.__dict__ else None,
        "ingredients": [ingredient.__dict__ for ingredient in recipe.ingredients],
        "created_at": recipe.created_at.astimezone(timezone).strftime("%d/%m/%Y")
    }

    return  recipe_formatted
