"""Model of an Employee"""

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class Employee(Base):
    """Defining a table for employees"""
    __tablename__ = "employees"
    id = Column(String(36), primary_key=True, default=uuid4)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    job_title = Column(String(30))
    phone_number = Column(String(50))

    user_id = Column(String(36), ForeignKey("users.id"))
    user = relationship("User", lazy='subquery')

    def __init__(self, first_name: str, last_name: str, job_title: str, phone_number: str, user_id: str):
        """Model of an Employee object"""
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.phone_number = phone_number
        self.user_id = user_id
