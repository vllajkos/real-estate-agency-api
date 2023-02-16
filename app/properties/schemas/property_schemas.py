from pydantic import BaseModel, UUID4

from app.properties.models import TypeOfProperty
from app.properties.schemas import TypeOfPropertySchema


class PropertySchemaOut(BaseModel):
    id: UUID4
    street: str
    municipality: str
    city: str
    country: str
    square_meters: float
    type_of_property_id: str
    type_of_property: TypeOfPropertySchema

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
