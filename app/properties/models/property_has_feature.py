"""
Model of relationship between concrete property made by user and features contained by property
"""
from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship

from app.db import Base


class PropertyHasFeature(Base):
    """Table and model for relationship between property and features contained by property"""

    __tablename__ = "properties_have_features"
    property_id = Column(String(36), ForeignKey("properties.id"), primary_key=True)
    feature_id = Column(String(36), ForeignKey("types_of_features.id"), primary_key=True)
    additional_feature_value = Column(Integer)
    __table_args__ = (PrimaryKeyConstraint(property_id, feature_id),)

    feature = relationship("TypeOfFeature", lazy="subquery")

    def __init__(self, property_id: str, feature_id: str, additional_feature_value: int) -> None:
        """Model of PropertyHasFeature object"""
        self.property_id = property_id
        self.feature_id = feature_id
        self.additional_feature_value = additional_feature_value
