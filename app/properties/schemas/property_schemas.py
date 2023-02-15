from pydantic import BaseModel, UUID4


class PropertySchemaOut(BaseModel):
    id: UUID4
    street: str
    municipality: str
    city: str
    country: str
    square_meters: float
    type_of_property_id: str

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
