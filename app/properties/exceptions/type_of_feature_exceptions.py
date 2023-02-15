class TypeOfFeatureExistsException(Exception):
    def __init__(self, status_code=400, message: str = "Type of feature already exists."):
        self.status_code = status_code
        self.message = message


class TypeOfFeatureDoesntExistException(Exception):
    def __init__(self, status_code=400, message: str = "Type of feature with provided information doesn't exist."):
        self.status_code = status_code
        self.message = message
