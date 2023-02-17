from pydantic import BaseModel


class EmployeeSchemaIn(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True


class EmployeeSchemaOut(BaseModel):
    id
    first_name: str
    last_name: str
    job_title: str
    phone_number: str
    user_id: str

    class Config:
        orm_mode = True
