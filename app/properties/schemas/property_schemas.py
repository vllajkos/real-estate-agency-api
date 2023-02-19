from typing import Optional

from pydantic import BaseModel, UUID4

from app.properties.models import TypeOfProperty
from app.properties.schemas import TypeOfPropertySchema
from app.properties.schemas.property_has_feature_schemas import PropertyHasFeatureSchemaOut


class PropertySchemaOut(BaseModel):
    id: UUID4
    street: str
    municipality: str
    city: str
    country: str
    square_meters: float
    # type_of_property_id: str
    type_of_property: TypeOfPropertySchema
    features: list[PropertyHasFeatureSchemaOut]

    class Config:
        orm_mode = True


class PropertySchemaIn(BaseModel):
    street: str
    municipality: str
    city: str
    country: str
    square_meters: float
    type_of_property_id: str

    class Config:
        orm_mode = True


class PropertySchemaFilter(BaseModel):
    municipality: Optional[str]
    city: Optional[str]
    country: Optional[str]
    min_square_meters: Optional[float]
    max_square_meters: Optional[float]
    type_of_property_id: Optional[str]

    class Config:
        orm_mode = True
