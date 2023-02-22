"""Client exceptions"""
from app.users.exceptions.custom_user_exception import CustomUserException


class ClientIdDoesntExistException(CustomUserException):
    status_code = 400
    message = "Provided client id doesnt exist."


class ClientExistWithProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "Client already exists with provided user id"


class ClientDoesntExistForProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "There is no client associated with provided user id"
