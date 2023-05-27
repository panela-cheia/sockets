aux1 = {
    "topic":"@user/create_user",
    "body":{
        "name":"João da Silva",
        "username":"@joaodasilva",
        "email":"joao.da.silva@gmail.com",
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
        "user_id":"823e3881-bda1-4f2a-9593-83c8d7fd0044",
        "follow_id":"5ca07281-0e46-4abc-8f1f-54b61ca27631"
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
        "photo": "96a89a09-6d2b-431f-8216-f5403b45cea3"
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
        "name":"dive-2",
        "description":"testar dive",
        "userId":"5229e1fa-5b96-48eb-bcec-49f4b413ea7b",
        "fileId":"ea86b599-dbdb-4ba6-8a1b-aca310150c4e",
        "ingredients":[
            {"name": "Ingredient 1", "amount": 1, "unit": "cup"},
            {"name": "Ingredient 2", "amount": 2, "unit": "teaspoon"},
            {"name": "Ingredient 3", "amount": 3, "unit": "gram"},
        ]
    }
}
 
# "diveId":"b9339c14-daba-4cc9-b736-50ac8da36d88",

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
        "name":"a"
    }
}

aux21 = {
    "topic":"@dive/enter_dive",
    "body":{
        "id":"75621072-e6b5-49ae-a5ff-424707d534b2",
        "diveId":"b9339c14-daba-4cc9-b736-50ac8da36d88"
    }
}

aux22 = {
    "topic":"@dive/exit_dive",
    "body":{
        "user":"f57255d9-afc0-478e-949b-0301f0bc05d0",
        "new_owner": None,
        "diveId":"4ebc6c64-7f1b-41f4-90e5-47c5e1456920"
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

aux25 = {
    "topic":"@user/search_users_user",
    "body":{
        "user_id":"75621072-e6b5-49ae-a5ff-424707d534b2",
        "value": "a"
    }
}

aux26 = {
    "topic": "@dive/users_dive",
    "body": {
        "user_id":"823e3881-bda1-4f2a-9593-83c8d7fd0044"
    }
}

aux27 = {
    "topic": "@dive/list_recipes_dive",
    "body": {
        "dive_id":"b9339c14-daba-4cc9-b736-50ac8da36d88"
    }
}

aux28 = {
    "topic":"@search/dive_and_users",
    "body":{
        "user_id":"75621072-e6b5-49ae-a5ff-424707d534b2",
        "value": "a"
    }
}