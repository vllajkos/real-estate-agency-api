"""Model of an Advertisement"""
from datetime import date
from uuid import uuid4

from sqlalchemy import Column, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship

from app.db import Base
from enum import Enum


class TypeOfAd(Enum):
    """Types of ads"""
    SALE = "sale"
    RENT = "rent"


class AdStatus(Enum):
    """Advertisement status"""
    ACTIVE = "active"
    PENDING = "pending"
    CANCELED = "canceled"
    REJECTED = "rejected"
    EXPIRED = "expired"
    FINALIZED = "finalized"


class Advertisement(Base):
    """Defining a table for advertisements"""
    __tablename__ = "advertisements"
    id = Column(String(50), primary_key=True, default=uuid4)
    type_of_ad = Column(String(20), nullable=False)
    start_date = Column(Date, default=date.today())
    price = Column(Float, nullable=False)
    description = Column(Text)
    status = Column(String(40), default=AdStatus.PENDING.value)

    property_id = Column(String(36), ForeignKey("properties.id"), nullable=False)
    client_id = Column(String(36), ForeignKey("clients.id"), nullable=False)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False)

    property = relationship("Property", lazy="subquery")
    client = relationship("Client", lazy="subquery")

    def __init__(self, type_of_ad: str, price: float, description: str, property_id: str,
                 client_id: str, employee_id: str, start_date: date = date.today(),
                 status: AdStatus = AdStatus.PENDING.value):
        """Model of an Advertisement object"""
        self.type_of_ad = type_of_ad
        self.price = price
        self.description = description
        self.property_id = property_id
        self.client_id = client_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.status = status
