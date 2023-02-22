"""Type of property Schemas"""
from pydantic import BaseModel, UUID4, StrictStr


class TypeOfPropertySchema(BaseModel):
    id: UUID4
    type_of_property: StrictStr

    class Config:
        orm_mode = True


class TypeOfPropertySchemaIn(BaseModel):
    type_of_property: StrictStr

    class Config:
        orm_mode = True
