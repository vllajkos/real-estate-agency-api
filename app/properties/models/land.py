"""Model of Land"""
from pydantic import UUID4
from sqlalchemy import String, Column, Float, ForeignKey

from app.db import Base


class Land(Base):
    """Defining table for lands"""
    __tablename__ = "lands"
    id = Column(String(50), primary_key=True, default=UUID4)
    street = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    type_of_land = Column(String(50),nullable=False)
    square_meters = Column(Float, nullable=False)

    client_id = Column(String(50), ForeignKey("clients.id"), nullable=False)
    ad_request_id = Column(String(50), ForeignKey("ad_requests.id"), nullable=False)

    def __init__(self, street: str, city: str, country: str, type_of_land: str, square_meters: float,
                 client_id: str, ad_request_id: str):
        """Model of a land object"""
        self.street = street
        self.city = city
        self.country = country
        self.type_of_land = type_of_land
        self.square_meters = square_meters
        self.client_id = client_id
        self.ad_request_id = ad_request_id
