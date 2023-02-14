from pydantic import BaseModel, UUID4


class TypeOfPropertySchema(BaseModel):
    id: UUID4
    type_of_property: str

    class Config:
        orm_mode = True


class TypeOfPropertySchemaIn(BaseModel):
    type_of_property: str

    class Config:
        orm_mode = True
