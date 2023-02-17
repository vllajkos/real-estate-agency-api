from datetime import date
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
    type_of_ad: str
    price: float
    description: str
    start_date: date
    status: str
    property: PropertySchemaOut
    client: ClientSchemaOut

    class Config:
        orm_mode = True
