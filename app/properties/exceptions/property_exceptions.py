from app.properties.exceptions.custom_property_exception import CustomPropertyException


class PropertiesNotFoundException(CustomPropertyException):
    status_code = 200
    message = "There are no properties of chosen type of property."


class PropertiesNotFoundByMunicipalityException(CustomPropertyException):
    status_code = 200
    message = "There are no properties for chosen municipality."


class PropertiesNotFoundByCityException(CustomPropertyException):
    status_code = 200
    message = "There are no properties for chosen city."


class PropertyNotFoundException(CustomPropertyException):
    status_code = 400
    message: str = "There is no property for provided id."
