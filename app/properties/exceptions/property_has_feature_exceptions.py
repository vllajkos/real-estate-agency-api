from app.properties.exceptions.custom_property_exception import CustomPropertyException


class PropertyAlreadyHasThatFeatureException(CustomPropertyException):
    status_code = 400
    message = "Property already has that feature. Pick another feature"
