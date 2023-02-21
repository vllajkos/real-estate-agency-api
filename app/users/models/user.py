"""Model of a User"""
from uuid import uuid4

from pydantic import UUID4
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.db import Base


class User(Base):
    """Defining a table for users"""
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=uuid4)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    active_status = Column(Boolean, default=True)
    superuser = Column(Boolean, default=False)

    def __init__(self, username: str, email: str, password: str, active_status: bool = True, superuser: bool = False):
        """Model of a User object"""
        self.username = username
        self.email = email
        self.password = password
        self.active_status = active_status
        self.superuser = superuser
