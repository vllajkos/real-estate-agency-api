from app.properties.exceptions.custom_property_exception import CustomPropertyException


class TypeOfPropertyExistsException(CustomPropertyException):
    status_code = 400
    message = "Type of property already exists."


class TypeOfPropertyDoesntExistException(CustomPropertyException):
    status_code = 400
    message = "Type of property with provided information doesn't exist."
