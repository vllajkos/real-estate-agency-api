from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, PrimaryKeyConstraint, Float
from app.db import Base


class PropertyHasFeature(Base):
    __tablename__ = "properties_have_features"
    property_id = Column(String(36), ForeignKey("properties.id"), primary_key=True)
    feature_id = Column(String(36), ForeignKey("types_of_features.id"), primary_key=True)
    feature_value = Column(Float)
    feature_unit = Column(String(50))
    __table_args__ = (PrimaryKeyConstraint(property_id, feature_id),)

    # UniqueConstraint("type_of_property_id", "feature_id", name="type_of_property_has_feature_unique_constraint"))

    def __init__(self, property_id: str, feature_id: str, feature_value: float, feature_unit: str):
        self.property_id = property_id
        self.feature_id = feature_id
        self.feature_value = feature_value
        self.feature_unit = feature_unit
