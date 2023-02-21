from app.users.exceptions.custom_user_exception import CustomUserException


class FollowDoesntExistException(CustomUserException):
    status_code = 400
    message = "Follow doesn't exist"


class FollowExistException(CustomUserException):
    status_code = 400
    message = "Follow exist"


class ClientsFollowingsException(CustomUserException):
    status_code = 400
    message = "Client doesn't have followings."


class AdFollowingsException(CustomUserException):
    status_code = 400
    message = "Advertisement doesn't have followings."
