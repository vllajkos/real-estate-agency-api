"""Model of an Advertisement"""

from pydantic import UUID4
from sqlalchemy import Column, String, Enum, Float, ForeignKey

from app.db import Base
import enum


class TypeOfAd(enum.Enum):
    """Types of ads"""
    SALE = "for sale"
    RENT = "for rent"


class Advetisement(Base):
    """Defining a table for advertisements"""
    __tablename__ = "advertisements"
    id = Column(String(50), primary_key=True, default=UUID4)
    type_of_ad = Column(Enum(TypeOfAd), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500))

    ad_request_id = Column(String(50), ForeignKey("ad_requests.id"), nullable=False)

    def __init__(self, type_of_ad: TypeOfAd, price: float, description: str, ad_request_id: UUID4):
        """Model of an Advertisement object"""
        self.type_of_ad = type_of_ad
        self.price = price
        self.description = description
        self.ad_request_id = ad_request_id
