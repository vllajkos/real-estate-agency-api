from pydantic import BaseModel, EmailStr


class UserSchemaIn(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserSchemaOut(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
