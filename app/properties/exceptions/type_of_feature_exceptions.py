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
