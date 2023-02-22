"""User exceptions"""
from app.users.exceptions.custom_user_exception import CustomUserException


class InvalidUsernameException(CustomUserException):
    status_code = 400
    message = "Username already in use. Choose another username."


class InvalidEmailException(CustomUserException):
    status_code = 400
    message = "Account exist for provided email. Forgot password?"


class UserIdDoesntExistException(CustomUserException):
    status_code = 400
    message = "Provided user id doesnt exist."


class InvalidPasswordException(CustomUserException):
    status_code = 401
    message = "Invalid password"


class InvalidLoginInfoException(CustomUserException):
    status_code = 401
    message = "Invalid username or email"


class CannotDeleteInUseException(CustomUserException):
    status_code = 400
    message = (
        "User has been posting ads, so his deletion would compromise data integrity in your database,"
        "it would be wiser to deactivate his account instead."
    )
