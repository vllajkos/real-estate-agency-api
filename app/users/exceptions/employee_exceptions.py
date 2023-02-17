from app.users.exceptions.custom_user_exception import CustomUserException


class EmployeeExistWithProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "Employee already exist with provided user id"
