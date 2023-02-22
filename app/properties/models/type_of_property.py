"""
Model for types of properties
"""
from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class TypeOfProperty(Base):
    """Modeling a table and a class for types of properties."""
    __tablename__ = "types_of_properties"
    id = Column(String(36), primary_key=True, default=uuid4)
    type_of_property = Column(String(60), unique=True, nullable=False)

    def __init__(self, type_of_property: str) -> None:
        """Model of a type of property object"""
        self.type_of_property = type_of_property


