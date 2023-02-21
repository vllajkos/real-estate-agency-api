class CustomAdvertisementExceptions(Exception):
    status_code = 400
    message = ""


class TypeOfAdExistsForPropertyException(CustomAdvertisementExceptions):
    status_code = 400
    message = "The property you are interested in advertising is currently listed " \
              "in our ads for the selected advertisement type and remains valid. " \
              "If you wish you can choose another type of advertisement for given property"


class AdNotFoundByFilteredParametersException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Advertisements not found for filter parameters"


class MinMaxPriceException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Min price cannot be greater than max price"


class PendingApprovalException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Advertisement with property id pending approval already."


class AdvertisementNoLongerActiveException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Advertisement is no longer active or is still pending approval."


class AdvertisementIdDoesntExistException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Advertisement id doesn't exist."


class NoExpiredAdsException(CustomAdvertisementExceptions):
    status_code = 400
    message = "No expired ads."


class AdNotPendingException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Ad not pending approval."


class NoPendingAdsException(CustomAdvertisementExceptions):
    status_code = 400
    message = "No pending ads for you"


class EnterValidStartEndDateException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Start date should represent date before end date."


class EnterValidDateFormatException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Enter date in valid format: YYYY-MM-DD."


class NotAuthorizedException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Not authorized to change status"


class NoAdsForClientIdException(CustomAdvertisementExceptions):
    status_code = 400
    message = "Provided client currently doesn't have active ads"
