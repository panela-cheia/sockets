aux1 = {
    "topic":"@user/create_user",
    "body":{
        "name":"teste",
        "username":"@teste",
        "email":"teste@gmail.com",
        "password":"12345678"
    }
}

aux2 = {
    "topic":"@user/login_with_email_user",
    "body":{
        "email":"teste@gmail.com",
        "password":"12345678"
    }
}

aux3 = {
    "topic":"@user/login_with_username_user",
    "body":{
        "username":"@teste",
        "password":"12345678"
    }
}

aux4 = {
    "topic":"@user/list_user",
    "body":{
    }
}

aux5 = {
    "topic":"@user/list_others_user",
    "body":{
        "id":"f98ae2bf-ea2e-4e0e-b6af-469c0193ea2d"
    }
}

aux6 = {
    "topic":"@user/follow_user",
    "body":{
        "user_id":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "follow_id":"f98ae2bf-ea2e-4e0e-b6af-469c0193ea2d"
    }
}

aux7 = {
    "topic":"@user/unfollow_user",
    "body":{
        "user_id":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "unfollow_id":"f98ae2bf-ea2e-4e0e-b6af-469c0193ea2d"
    }
}

aux8 = {
    "topic":"@user/update_user",
    "body":{
        "id":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "bio":"amo comer!",
        "name": "Vinicius Mendes",
        "username": "@vinicmendes"
    }
}

aux9 = {
    "topic":"@user/update_photo_user",
    "body":{
        "id":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "photo": "51ce99f5-0223-4c63-b57e-24de13f37038"
    }
}

aux10 = {
    "topic":"@file/create_file",
    "body":{
        "name":"file.png"
    }
}

aux11 = {
    "topic":"@file/delete_file",
    "body":{
        "id":"f16c8840-5c8c-4481-9dd4-0952583eb609"
    }
}

aux12 = {
    "topic":"@barn/save_recipe_barn",
    "body":{
        "id":"45e10356-681a-4593-a438-9ec90871c804",
        "recipe_id":"d63222be-f90d-4e1b-a39f-bbb741fc3af0"
    }
}

aux13 = {
    "topic":"@barn/search_recipe_barn",
    "body":{
        "id":"45e10356-681a-4593-a438-9ec90871c804",
        "name":"Receita"
    }
}

aux14 = {
    "topic":"@barn/remove_recipe_barn",
    "body":{
        "id":"45e10356-681a-4593-a438-9ec90871c804",
        "recipe_id":"d63222be-f90d-4e1b-a39f-bbb741fc3af0"
    }
}

aux15 = {
    "topic":"@recipe/create_recipe",
    "body":{
        "name":"New",
        "description":"new recipe",
        "userId":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "fileId":"51ce99f5-0223-4c63-b57e-24de13f37038",
        "ingredients":[
            {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
            {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
            {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
        ]
    }
}

aux16 = {
    "topic":"@recipe/list_recipe",
    "body":{
    }
}

aux17 = {
    "topic":"@recipe/reaction_recipe",
    "body":{
        "type":"bão",
        "recipe_id":"d63222be-f90d-4e1b-a39f-bbb741fc3af0",
        "user_id":"9badd489-fe3f-4b93-a20d-caaa621d4213"
    }
}

aux18 = {
    "topic":"@recipe/search_recipe",
    "body":{
        "name":"New"
    }
}

aux19 = {
    "topic":"@dive/create_dive",
    "body":{
        "name":"lele",
        "description":"Buteco do Zé2",
        "fileId":"51ce99f5-0223-4c63-b57e-24de13f37038",
        "userId":"15559c81-0d4a-47b8-ba7a-a468b62e7217"
    }
}

aux20 = {
    "topic":"@dive/search_dive",
    "body":{
        "name":"buteco"
    }
}

aux21 = {
    "topic":"@dive/enter_dive",
    "body":{
        "id":"aea42f09-5372-4ed2-ad49-dbc65e327dcb",
        "diveId":"76806064-77aa-4570-b85f-5f87d1152338"
    }
}

aux22 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"9badd489-fe3f-4b93-a20d-caaa621d4213",
        "new_owner":"15559c81-0d4a-47b8-ba7a-a468b62e7217",
        "diveId":"76806064-77aa-4570-b85f-5f87d1152338"
    }
}

aux23 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"9badd489-fe3f-4b93-a20d-caaa621d4213",
        "new_owner":"aea42f09-5372-4ed2-ad49-dbc65e327dcb",
        "diveId":"76806064-77aa-4570-b85f-5f87d1152338"
    }
}

aux24 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"9badd489-fe3f-4b93-a20d-caaa621d4213",
        "new_owner":"",
        "diveId":"76806064-77aa-4570-b85f-5f87d1152338"
    }
}