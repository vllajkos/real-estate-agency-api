"""Client schemas"""
from pydantic import BaseModel, StrictStr
from app.users.schemas.user_schemas import UserSchemaOut


class ClientSchemaIn(BaseModel):
    first_name: StrictStr
    last_name: StrictStr
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True


class ClientSchemaOut(BaseModel):
    id: str
    first_name: StrictStr
    last_name: StrictStr
    phone_number: str
    user_id: str

    user: UserSchemaOut

    class Config:
        orm_mode = True
