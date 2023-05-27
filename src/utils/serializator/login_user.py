def loginUserSerializator(user,token):
    response = {
        "user":{
            "id":user.id,
            "name":user.name,
            "username":user.username,
            "email":user.email
        },
        "token":token.decode('utf-8')
    }

    return response