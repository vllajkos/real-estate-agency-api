from pydantic import BaseModel


class ClientSchemaIn(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True


class ClientSchemaOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True
