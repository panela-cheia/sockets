import pytz

timezone = pytz.timezone('America/Sao_Paulo')

def recipeSerializator(recipe):
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

def userProfileSerializator(user):
    
    recipes = []

    for recipe in user.recipes:
        recipes.append(recipeSerializator(recipe=recipe))

    data = {
        "id": user.id,
        "name": user.name,
        "bio": user.bio,
        "photo": {
            "id": user.photo.id,
            "name": user.photo.name,
            "path": user.photo.path
        } if user.photo else None,
        "posts": str(len(user.recipes)) + " posts",
        "following":str(len(user.following)) + " seguindo",
        "followers":str(len(user.followers)) + " seguidores",
        "recipes":recipes
    }

    return data