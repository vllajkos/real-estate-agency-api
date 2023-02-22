"""Advertisement schemas"""
from datetime import date
from typing import Optional
from pydantic import BaseModel, PositiveFloat, PositiveInt
from app.properties.schemas import PropertySchemaOut
from app.users.schemas import ClientSchemaOut


class AdvertisementSchemaIn(BaseModel):
    price: PositiveFloat
    description: Optional[str]
    property_id: str
    client_id: str

    class Config:
        orm_mode = True


class AdvertisementSchemaOut(BaseModel):
    id: str
    type_of_ad: str
    price: PositiveFloat
    description: str
    admission_date: date
    status_date: Optional[date]
    status: str
    property: PropertySchemaOut
    client: ClientSchemaOut

    class Config:
        orm_mode = True


class FilterSchemaIn(BaseModel):
    type_of_ad: Optional[str]
    min_price: Optional[PositiveFloat]
    max_price: Optional[PositiveFloat]
    municipality: Optional[str]
    city: Optional[str]
    country: Optional[str]
    min_square_meters: Optional[PositiveFloat]
    max_square_meters: Optional[PositiveFloat]
    type_of_property_id: Optional[str]
    feature_id_list: Optional[list[str]]
    features_id_operator_value_list: Optional[list[tuple[str, str, PositiveInt]]]

    class Config:
        orm_mode = True
