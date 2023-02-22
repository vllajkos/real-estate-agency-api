"""Type of property has type of features Exceptions"""
from app.properties.exceptions.custom_property_exception import CustomPropertyException


class TypeOfPropertyHasFeatureExistsException(CustomPropertyException):
    status_code = 400
    message = "Provided type of property already has given feature."


class TypeOfPropertyDoesntHaveFeaturesException(CustomPropertyException):
    status_code = 400
    message = "Type of property doesn't have features."


class TypeOfPropertyDoesntSupportFeatureException(CustomPropertyException):
    status_code = 400
    message = "Type of property doesn't support given feature."
