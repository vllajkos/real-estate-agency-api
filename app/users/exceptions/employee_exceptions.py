from app.users.exceptions.custom_user_exception import CustomUserException


class EmployeeExistWithProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "Employee already exist with provided user id"


class NoEmployeesYetException(CustomUserException):
    status_code = 400
    message = "No employees yet to accept ad for review"


class EmployeeIdDoesntExistException(CustomUserException):
    status_code = 400
    message = "Employee id doesn't exist"


class EmployeeDoesntExistforProvidedUserIdException(CustomUserException):
    status_code = 400
    message = "Employee doesn't exist for provided user id"
