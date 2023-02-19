from pydantic import BaseModel

from app.properties.schemas import TypeOfFeatureSchema


class TypeOfPropertyHasFeatureSchemaIn(BaseModel):
    type_of_property_id: str
    feature_id: str

    class Config:
        orm_mode = True


class TypeOfPropertyHasFeatureSchemaOut(BaseModel):
    feature: TypeOfFeatureSchema

    class Config:
        orm_mode = True
