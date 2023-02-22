"""Property has feature Exceptions"""
from app.properties.exceptions.custom_property_exception import CustomPropertyException


class PropertyAlreadyHasThatFeatureException(CustomPropertyException):
    status_code = 400
    message = "Property already has that feature. Pick another feature"


class PropertyDoesntHaveFeaturesException(CustomPropertyException):
    status_code = 200
    message = "Property doesn't have features"


class PropertyDoesntHaveRequestedFeatureException(CustomPropertyException):
    status_code = 200
    message = "Property doesn't have requested feature"
