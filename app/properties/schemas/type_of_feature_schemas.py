from pydantic import BaseModel, UUID4


class TypeOfFeatureSchemaOut(BaseModel):
    id: UUID4
    feature: str

    class Config:
        orm_mode = True


class TypeOfFeatureSchemaIn(BaseModel):
    feature: str

    class Config:
        orm_mode = True
