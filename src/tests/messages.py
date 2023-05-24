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