"""Type of feature Schemas"""
from pydantic import UUID4, BaseModel, StrictStr


class TypeOfFeatureSchemaOut(BaseModel):
    id: UUID4
    feature: StrictStr

    class Config:
        orm_mode = True


class TypeOfFeatureSchemaIn(BaseModel):
    feature: StrictStr
    optional_values: bool

    class Config:
        orm_mode = True


class TypeOfFeatureSchema(BaseModel):
    id: UUID4
    feature: StrictStr
    optional_values: bool

    class Config:
        orm_mode = True
