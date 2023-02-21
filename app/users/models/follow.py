"""Model of a Follow class which represents clients desires towards certain ads"""

from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, PrimaryKeyConstraint

from app.db import Base


class Follow(Base):
    """Defining a table for follows"""
    __tablename__ = "follows"
    client_id = Column(String(36), ForeignKey("clients.id"), primary_key=True)
    advertisement_id = Column(String(36), ForeignKey("advertisements.id"), primary_key=True)

    __table_args__ = (PrimaryKeyConstraint("client_id", "advertisement_id", name="follows_uc"),)

    def __init__(self, client_id: str, advertisement_id: str):
        """Model of a Follow object"""
        self.client_id = client_id
        self.advertisement_id = advertisement_id
