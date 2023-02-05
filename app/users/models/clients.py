"""Model of a Client"""

from pydantic import UUID4
from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base


class Client(Base):
    """Defining a table for clients"""
    __tablename__ = "clients"
    id = Column(String(50), primary_key=True, default=UUID4)
    first_name = Column(String(30))
    last_name = Column(String(30))
    jmbg = Column(String(13))
    phone_number = Column(String(50))

    user_id = Column(String(50), ForeignKey("users.id"))
    user = relationship("User", lazy='subquery')

    def __init__(self, first_name: str, last_name: str, jmbg: str, phone_number: str):
        """Model of a Client object"""
        self.first_name = first_name
        self.last_name = last_name
        self.jmbg = jmbg
        self.phone_number = phone_number
