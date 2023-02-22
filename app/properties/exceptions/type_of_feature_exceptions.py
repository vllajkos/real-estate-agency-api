"""Type of feature Exceptions"""
from app.properties.exceptions.custom_property_exception import CustomPropertyException


class TypeOfFeatureExistsException(CustomPropertyException):
    status_code = 400
    message = "Type of feature already exists."


class TypeOfFeatureDoesntExistException(CustomPropertyException):
    status_code = 400
    message = "Type of feature with provided information doesn't exist."


class TypeOfFeatureDoesntSupportAdditionalValueException(CustomPropertyException):
    status_code = 400
    message = "Type of feature doesn't support additional value parameters."


class TypeOfFeatureDeleteException(CustomPropertyException):
    status_code = 400
    message = (
        "Deletion is available only after creation of type of feature if you made some kind"
        "of mistake and before type of feature is being used. It is advised"
        "not to delete it after use because it will corrupt data integrity of your database."
        "You can unlink chosen type of feature from available types of properties so it won't be available "
        "anymore."
    )
