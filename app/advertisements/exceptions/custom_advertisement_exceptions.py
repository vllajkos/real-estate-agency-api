class CustomAdvertisementExceptions(Exception):
    status_code = 400
    message = ""


class TypeOfAdExistsForPropertyException(CustomAdvertisementExceptions):
    status_code = 400
    message = "The property you are interested in advertising is currently listed " \
              "in our ads for the selected advertisement type and remains valid. " \
              "If you wish you can choose another type of advertisement for given property"
