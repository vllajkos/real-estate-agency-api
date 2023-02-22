"""Type of property Exceptions"""
from app.properties.exceptions.custom_property_exception import CustomPropertyException


class TypeOfPropertyExistsException(CustomPropertyException):
    status_code = 400
    message = "Type of property already exists."


class TypeOfPropertyDoesntExistException(CustomPropertyException):
    status_code = 400
    message = "Type of property with provided information doesn't exist."


class TypeOfPropertyDeleteException(CustomPropertyException):
    status_code = 400
    message = "Deletion is available only after creation of type of property if you made some kind" \
              "of mistake and before type of property is being used. It is advised" \
              "not to delete it after use because it will corrupt data integrity of your database." \
              "You can unlink chosen type of property from available features so it won't be available " \
              "anymore."
