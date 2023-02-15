class TypeOfPropertyHasFeatureExistsException(Exception):
    def __init__(self, status_code=400, message: str = "Provided type of property already has given feature."):
        self.status_code = status_code
        self.message = message


class TypeOfPropertyDoesntHaveFeaturesException(Exception):
    def __init__(self, status_code=400, message: str = "Type of property doesn't have features."):
        self.status_code = status_code
        self.message = message


class TypeOfPropertyDoesntHaveFeatureException(Exception):
    def __init__(self, status_code=400, message: str = "Type of property doesn't have given feature."):
        self.status_code = status_code
        self.message = message
