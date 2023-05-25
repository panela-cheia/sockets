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
        "id":"f57255d9-afc0-478e-949b-0301f0bc05d0"
    }
}

aux6 = {
    "topic":"@user/follow_user",
    "body":{
        "user_id":"5ca07281-0e46-4abc-8f1f-54b61ca27631",
        "follow_id":"f57255d9-afc0-478e-949b-0301f0bc05d0"
    }
}

aux7 = {
    "topic":"@user/unfollow_user",
    "body":{
        "user_id":"5ca07281-0e46-4abc-8f1f-54b61ca27631",
        "unfollow_id":"f57255d9-afc0-478e-949b-0301f0bc05d0"
    }
}

aux8 = {
    "topic":"@user/update_user",
    "body":{
        "id":"75621072-e6b5-49ae-a5ff-424707d534b2",
        "bio":"amo comer!",
        "name": "Vinicius Mendes",
        "username": "@vinicmendes"
    }
}

aux9 = {
    "topic":"@user/update_photo_user",
    "body":{
        "id":"823e3881-bda1-4f2a-9593-83c8d7fd0044",
        "photo": "9efa6ab2-f2c0-4985-b4ff-a66f07377fd5"
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
        "id":"f5881021-ab63-46d5-bce2-dfe91c5c1111"
    }
}

aux12 = {
    "topic":"@barn/save_recipe_barn",
    "body":{
        "id":"fdbe4ceb-2895-40bb-bc19-55190ee3f555",
        "recipe_id":"9994cd6f-1b2e-4456-93f7-6bff90a19fb3"
    }
}

aux13 = {
    "topic":"@barn/search_recipe_barn",
    "body":{
        "id":"fdbe4ceb-2895-40bb-bc19-55190ee3f555",
        "name":"Receita"
    }
}

aux14 = {
    "topic":"@barn/remove_recipe_barn",
    "body":{
        "id":"fdbe4ceb-2895-40bb-bc19-55190ee3f555",
        "recipe_id":"9994cd6f-1b2e-4456-93f7-6bff90a19fb3"
    }
}

aux15 = {
    "topic":"@recipe/create_recipe",
    "body":{
        "name":"New",
        "description":"new recipe",
        "userId":"f57255d9-afc0-478e-949b-0301f0bc05d0",
        "fileId":"39daafaf-06cd-475d-818d-717942c16506",
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
        "recipe_id":"ab066eb8-0f05-434d-abad-fc1a8027d94f",
        "user_id":"5ca07281-0e46-4abc-8f1f-54b61ca27631"
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
        "name":"Açai",
        "description":"açai é legal, nutela é legal!",
        "fileId":"4a3dbb52-1076-4ef4-9c5e-306cf785091b",
        "userId":"f57255d9-afc0-478e-949b-0301f0bc05d0"
    }
}

aux20 = {
    "topic":"@dive/search_dive",
    "body":{
        "name":"Bte"
    }
}

aux21 = {
    "topic":"@dive/enter_dive",
    "body":{
        "id":"823e3881-bda1-4f2a-9593-83c8d7fd0044",
        "diveId":"b9339c14-daba-4cc9-b736-50ac8da36d88"
    }
}

aux22 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"823e3881-bda1-4f2a-9593-83c8d7fd0044",
        "new_owner": None,
        "diveId":"b9339c14-daba-4cc9-b736-50ac8da36d88"
    }
}

aux23 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"f57255d9-afc0-478e-949b-0301f0bc05d0",
        "new_owner":"823e3881-bda1-4f2a-9593-83c8d7fd0044",
        "diveId":"b9339c14-daba-4cc9-b736-50ac8da36d88"
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