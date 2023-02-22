"""Hardcoded data"""
from enum import Enum

EXPIRES_IN_DAYS = 30
STATS_PERIOD = 30


class TypeOfAd(Enum):
    SALE = "sale"
    RENT = "rent"


class MoreLessEqual(Enum):
    MORE = ">"
    LESS = "<"
    EQUAL = "="


class UserAdStatus(Enum):
    CANCELED = "canceled"
    SOLD_RENTED = "sold/rented"


class EmployeeAdStatus(Enum):
    ACTIVE = "active"
    REJECTED = "rejected"


class AdStatus(Enum):
    ACTIVE = "active"
    PENDING = "pending"
    CANCELED = "canceled"
    REJECTED = "rejected"
    EXPIRED = "expired"
    SOLD_RENTED = "sold/rented"


class SortByPrice(Enum):
    LOW = "from lowest to highest"
    HIGH = "from highest to lowest"
