"""Model of a Client"""
from uuid import uuid4

from pydantic import UUID4
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Client(Base):
    """Defining a table for clients"""
    __tablename__ = "clients"
    id = Column(String(36), primary_key=True, default=uuid4)
    first_name = Column(String(30))
    last_name = Column(String(30))
    phone_number = Column(String(50))

    user_id = Column(String(36), ForeignKey("users.id"), unique=True)
    user = relationship("User", lazy='subquery')

    def __init__(self, first_name: str, last_name: str, phone_number: str, user_id: str):
        """Model of a Client object"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.user_id = user_id
