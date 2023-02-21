from pydantic import BaseModel

from app.users.schemas.user_schemas import UserSchemaOut


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

    user: UserSchemaOut

    class Config:
        orm_mode = True
