from pydantic import BaseModel


class FollowSchema(BaseModel):
    client_id: str
    advertisement_id: str

    class Config:
        orm_mode = True
