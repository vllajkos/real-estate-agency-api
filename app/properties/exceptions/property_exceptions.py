class PropertiesNotFoundException(Exception):
    def __init__(self, status_code=200, message: str = "There are no properties of chosen type of property."):
        self.status_code = status_code
        self.message = message


class PropertiesNotFoundByMunicipalityException(Exception):
    def __init__(self, status_code=200, message: str = "There are no properties for chosen municipality."):
        self.status_code = status_code
        self.message = message


class PropertiesNotFoundByCityException(Exception):
    def __init__(self, status_code=200, message: str = "There are no properties for chosen city."):
        self.status_code = status_code
        self.message = message


class PropertyNotFoundException(Exception):
    def __init__(self, status_code=400, message: str = "There is no property for provided id."):
        self.status_code = status_code
        self.message = message
