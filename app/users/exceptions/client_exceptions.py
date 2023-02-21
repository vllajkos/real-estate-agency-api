from app.users.exceptions.custom_user_exception import CustomUserException


# class InvalidUsernameException(CustomUserException):
#     status_code = 400
#     message = "Username already in use. Choose another username."
#
#
# class InvalidEmailException(CustomUserException):
#     status_code = 400
#     message = "Account exist for provided email. Forgot password?"


class ClientIdDoesntExistException(CustomUserException):
    status_code = 400
    message = "Provided client id doesnt exist."


class ClientExistWithProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "Client already exists with provided user id"


#
#
# class InvalidLoginInfoException(CustomUserException):
#     status_code = 401
#     message = "Invalid username or email"

class ClientDoesntExistForProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "There is no client associated with provided user id"
