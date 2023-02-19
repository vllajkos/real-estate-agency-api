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


class MinMaxSquareMetersException(CustomPropertyException):
    status_code = 400
    message = "Minimum square meters is not allowed to be greater than maximum square meters"


class PropertiesNotFoundByFilterParametersException(CustomPropertyException):
    status_code = 400
    message = "Properties not found for filter parameters"

class NoPropertyException(CustomPropertyException):
    status_code = 400
    message = "Properties doesnt "
