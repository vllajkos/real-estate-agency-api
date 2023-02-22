"""
Model representing which type of property can contain which type of feature
"""
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from app.db import Base


class TypeOfPropertyHasFeature(Base):
    """Model of a table and object of which type of property can contain which type of feature"""

    __tablename__ = "type_of_property_has_feature"
    type_of_property_id = Column(String(36), ForeignKey("types_of_properties.id"), primary_key=True)
    feature_id = Column(String(36), ForeignKey("types_of_features.id"), primary_key=True)
    __table_args__ = (PrimaryKeyConstraint(type_of_property_id, feature_id),)

    feature = relationship("TypeOfFeature", lazy="subquery")

    def __init__(self, type_of_property_id: str, feature_id: str) -> None:
        """Model for TypeOfPropertyHasFeature object"""
        self.type_of_property_id = type_of_property_id
        self.feature_id = feature_id
