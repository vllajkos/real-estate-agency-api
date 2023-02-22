"""Follow schemas"""
from pydantic import BaseModel
from app.advertisements.schemas import AdvertisementSchemaOut
from app.users.schemas import ClientSchemaOut


class FollowSchema(BaseModel):
    client_id: str
    advertisement_id: str

    class Config:
        orm_mode = True


class FollowForClientSchema(BaseModel):
    advertisements: AdvertisementSchemaOut

    class Config:
        orm_mode = True


class FollowForAdSchema(BaseModel):
    clients: ClientSchemaOut

    class Config:
        orm_mode = True
