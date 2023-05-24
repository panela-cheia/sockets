from enum import Enum

class Topics(str,Enum):
    USER_CREATE = "@user/create_user"
    USER_LOGIN_EMAIL = "@user/login_with_email_user"
    USER_LOGIN_USERNAME = "@user/login_with_username_user"
    USER_LIST = "@user/list_user"
    USER_LIST_OTHERS = "@user/list_others_user"
    USER_FOLLOW = "@user/follow_user"
    USER_UNFOLLOW = "@user/unfollow_user"
    USER_UPDATE = "@user/update_user"
    USER_UPDATE_PHOTO = "@user/update_photo_user"

    BARN_SEARCH_RECIPE = "@barn/search_recipe_barn"
    BARN_SAVE_RECIPE = "@barn/save_recipe_barn"
    BARN_REMOVE_RECIPE = "@barn/remove_recipe_barn"

    FILE_CREATE = "@file/create_file"
    FILE_DELETE = "@file/delete_file"

    RECIPE_CREATE = "@recipe/create_recipe"
    RECIPE_LIST = "@recipe/list_recipe"
    RECIPE_REACTION = "@recipe/reaction_recipe"
    RECIPE_SEARCH = "@recipe/search_recipe"

    DIVE_CREATE = "@dive/create_dive"
    DIVE_SEARCH = "@dive/search_dive"
    DIVE_ENTER = "@dive/enter_dive"
    DIVE_EXIT = "@dive/exit_dive"
    DIVE_UPDATE = "@dive/update_dive"