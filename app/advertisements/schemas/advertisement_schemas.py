from datetime import date
from typing import Optional

from pydantic import BaseModel
from app.properties.schemas import PropertySchemaOut
from app.users.schemas import ClientSchemaOut


class AdvertisementSchemaIn(BaseModel):
    price: float
    description: str
    property_id: str
    client_id: str

    class Config:
        orm_mode = True


class AdvertisementSchemaOut(BaseModel):
    id: str
    type_of_ad: str
    price: float
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
    min_price: Optional[float]
    max_price: Optional[float]
    municipality: Optional[str]
    city: Optional[str]
    country: Optional[str]
    min_square_meters: Optional[float]
    max_square_meters: Optional[float]
    type_of_property_id: Optional[str]
    feature_id_list: Optional[list[str]]
    features_id_operator_value_list: Optional[list[tuple[str, str, int]]]

    class Config:
        orm_mode = True
