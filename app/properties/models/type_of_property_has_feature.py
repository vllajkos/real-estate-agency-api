from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, PrimaryKeyConstraint

from app.db import Base


class TypeOfPropertyHasFeature(Base):
    __tablename__ = "type_of_property_has_feature"
    type_of_property_id = Column(String(36), ForeignKey("types_of_properties.id"), primary_key=True)
    feature_id = Column(String(36), ForeignKey("types_of_features.id"), primary_key=True)
    __table_args__ = (PrimaryKeyConstraint(type_of_property_id, feature_id),)

    # UniqueConstraint("type_of_property_id", "feature_id", name="type_of_property_has_feature_unique_constraint"))

    def __init__(self, type_of_property_id: str, feature_id: str):
        self.type_of_property_id = type_of_property_id
        self.feature_id = feature_id
