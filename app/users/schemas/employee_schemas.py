"""Employee schemas"""
from pydantic import BaseModel, StrictStr
from app.users.schemas import UserSchemaOut


class EmployeeSchemaIn(BaseModel):
    first_name: StrictStr
    last_name: StrictStr
    job_title: StrictStr
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaOut(BaseModel):
    id: str
    first_name: StrictStr
    last_name: StrictStr
    job_title: StrictStr
    phone_number: str
    user_id: str

    user: UserSchemaOut

    class Config:
        orm_mode = True
