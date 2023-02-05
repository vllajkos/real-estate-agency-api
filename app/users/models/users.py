"""Model of a User"""

from pydantic import UUID4
from sqlalchemy import Column, String, Boolean

from app.db import Base


class User(Base):
    """Defining a table for users"""
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=UUID4)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50),  nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __init__(self, username: str, email: str, password: str, is_active: bool = True, is_superuser: bool = False):
        """Model of a User object"""
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_superuser = is_superuser
