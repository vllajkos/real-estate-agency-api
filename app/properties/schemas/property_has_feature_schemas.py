"""Property has feature Schemas"""
from typing import Optional

from pydantic import BaseModel, PositiveInt

from app.properties.schemas import TypeOfFeatureSchemaOut


class PropertyHasFeatureSchemaWithADIn(BaseModel):
    property_id: str
    feature_id: str
    additional_feature_value: PositiveInt

    class Config:
        orm_mode = True


class PropertyHasFeatureSchemaWithoutAVIn(BaseModel):
    property_id: str
    feature_id: str

    class Config:
        orm_mode = True


class PropertyHasFeatureSchemaOut(BaseModel):
    feature: TypeOfFeatureSchemaOut
    additional_feature_value: Optional[PositiveInt]

    class Config:
        orm_mode = True


class PropertyHasFeatureSchemaWAVOut(BaseModel):
    feature: TypeOfFeatureSchemaOut

    class Config:
        orm_mode = True
