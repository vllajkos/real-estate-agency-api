from typing import Optional

from pydantic import PositiveInt, BaseModel


class PropertyHasFeatureSchemaIn(BaseModel):
    property_id: str
    feature_id: str
    additional_feature_value: Optional[PositiveInt]

    class Config:
        orm_mode = True


class PropertyHasFeatureSchemaOut(BaseModel):
    property_id: str
    feature_id: str
    additional_feature_value: Optional[PositiveInt]

    class Config:
        orm_mode = True
