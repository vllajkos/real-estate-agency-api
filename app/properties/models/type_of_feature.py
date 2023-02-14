"""Model of a type of feature"""
from uuid import uuid4
from sqlalchemy import Column, String
from app.db import Base


class TypeOfFeature(Base):
    """Modeling a table and a class for types of features."""
    __tablename__ = "types_of_features"
    id = Column(String(36), primary_key=True, default=uuid4)
    feature = Column(String(60), unique=True)

    def __init__(self, feature: str) -> None:
        """Model of a type of feature object"""
        self.feature = feature
