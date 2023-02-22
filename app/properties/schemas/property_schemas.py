"""Property Schemas"""
from typing import Optional
from pydantic import BaseModel, UUID4, PositiveFloat, StrictStr, NonNegativeFloat
from app.properties.schemas import TypeOfPropertySchema
from app.properties.schemas.property_has_feature_schemas import PropertyHasFeatureSchemaOut


class PropertySchemaOut(BaseModel):
    id: UUID4
    street: str
    municipality: StrictStr
    city: StrictStr
    country: StrictStr
    square_meters: PositiveFloat
    type_of_property: TypeOfPropertySchema
    features: list[PropertyHasFeatureSchemaOut]

    class Config:
        orm_mode = True


class PropertySchemaIn(BaseModel):
    street: str
    municipality: StrictStr
    city: StrictStr
    country: StrictStr
    square_meters: PositiveFloat
    type_of_property_id: str

    class Config:
        orm_mode = True


class PropertySchemaFilter(BaseModel):
    municipality: Optional[StrictStr]
    city: Optional[StrictStr]
    country: Optional[StrictStr]
    min_square_meters: Optional[NonNegativeFloat]
    max_square_meters: Optional[PositiveFloat]
    type_of_property_id: Optional[str]

    class Config:
        orm_mode = True
