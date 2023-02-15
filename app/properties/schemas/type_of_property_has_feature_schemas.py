from pydantic import BaseModel


class TypeOfPropertyHasFeatureSchema(BaseModel):
    type_of_property_id: str
    feature_id: str

    class Config:
        orm_mode = True

