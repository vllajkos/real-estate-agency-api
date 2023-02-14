class TypeOfPropertyExistsException(Exception):
    def __init__(self, status_code=400, message: str = "Type of property already exists."):
        self.status_code = status_code
        self.message = message


class TypeOfPropertyDoesntExistsException(Exception):
    def __init__(self, status_code=400, message: str = "Type of property with provided information doesn't exist."):
        self.status_code = status_code
        self.message = message
