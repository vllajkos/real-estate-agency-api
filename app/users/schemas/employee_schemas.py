from pydantic import BaseModel

from app.users.schemas import UserSchemaOut


class EmployeeSchemaIn(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    job_title: str
    phone_number: str
    user_id: str

    user: UserSchemaOut

    class Config:
        orm_mode = True
