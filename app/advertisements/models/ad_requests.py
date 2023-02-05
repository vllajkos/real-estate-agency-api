"""Model of an Advertisement Request for approval made by Client for an Employee"""
import enum
from datetime import datetime

from pydantic import UUID4
from sqlalchemy import Column, String, ForeignKey, Enum, Date

from app.db import Base


class RequestStatus(enum.Enum):
    """Types of status requests"""
    APPROVED = "approved"
    PENDING = "pending"
    REJECTED = "rejected"


class AdRequest(Base):
    """Defining a table for advertisement requests"""
    __tablename__ = "ad_requests"
    id = Column(String(50), primary_key=True, default=UUID4)
    request_date = Column(Date)
    # nisam siguran da moze enum ovako da se iskoristi, provericu
    request_status = Column(Enum(RequestStatus), default=RequestStatus.PENDING)

    employee_id = Column(String(50), ForeignKey("employees.id"), nullable=False)

    def __init__(self, employee_id: str, request_date: str, request_status: str = RequestStatus.PENDING):
        """Model of an Advertisement Request object"""
        self.request_date = datetime.strptime(request_date, "%Y-%m-%d")
        self.request_status = request_status
        self.employee_id = employee_id
