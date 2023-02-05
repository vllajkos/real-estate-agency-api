"""Model of an Apartment"""

from pydantic import UUID4
from sqlalchemy import String, Column, Float, Integer, Boolean, ForeignKey

from app.db import Base


class Apartment(Base):
    """Definign a table for apartments"""
    __tablename__ = "apartments"
    id = Column(String(50), primary_key=True, default=UUID4)
    street = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    square_meters = Column(Float, nullable=False)
    floor = Column(Integer, nullable=False)
    rooms = Column(Integer, nullable=False)
    terrace = Column(Boolean, default=False)
    parking_space = Column(Boolean, default=False)
    air_conditioning = Column(Boolean, default=False)
    heating = Column(Boolean, default=False)

    client_id = Column(String(50), ForeignKey("clients.id"), nullable=False)
    ad_request_id = Column(String(50), ForeignKey("ad_requests.id"), nullable=False)

    def __init__(self, street: str, city: str, country: str, square_meters: float, floor: int, rooms: int,
                 terrace: bool, parking_space: bool, air_conditioning: bool, heating: bool,
                 client_id: str, ad_request_id: str):
        """Model of an Apartment object"""
        self.street = street
        self.city = city
        self.country = country
        self.square_meters = square_meters
        self.floor = floor
        self.rooms = rooms
        self.terrace = terrace
        self.parking_space = parking_space
        self.air_conditioning = air_conditioning
        self.heating = heating
        self.client_id = client_id
        self.ad_request_id = ad_request_id
