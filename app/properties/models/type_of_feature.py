"""
Model of a type of feature
"""
from uuid import uuid4

from sqlalchemy import Boolean, Column, String

from app.db import Base


class TypeOfFeature(Base):
    """Modeling a table and a class for types of features."""

    __tablename__ = "types_of_features"
    id = Column(String(36), primary_key=True, default=uuid4)
    feature = Column(String(60), unique=True, nullable=False)
    optional_values = Column(Boolean, nullable=False)

    def __init__(self, feature: str, optional_values: bool) -> None:
        """Model of a type of feature object"""
        self.feature = feature
        self.optional_values = optional_values
