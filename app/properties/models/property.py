from uuid import uuid4
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Property(Base):
    """Modeling a table and a class for properties."""
    __tablename__ = "properties"
    id = Column(String(36), primary_key=True, default=uuid4)
    street = Column(String(100), nullable=False)
    municipality = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    square_meters = Column(Float, nullable=False)

    type_of_property_id = Column(String(36), ForeignKey("types_of_properties.id"), nullable=False)
    type_of_property = relationship("TypeOfProperty", lazy="subquery")
    features = relationship("PropertyHasFeature", lazy="subquery")

    def __init__(self, street: str, municipality: str, city: str, country: str, square_meters: float,
                 type_of_property_id: str) -> None:
        """Model of a property object"""
        self.street = street
        self.municipality = municipality
        self.city = city
        self.country = country
        self.square_meters = square_meters
        self.type_of_property_id = type_of_property_id
