"""Session maker"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

MYSQL_URL = (
    f"{settings.DB_HOST}://{settings.DB_USER}:{settings.DB_PASSWORD}@"
    f"{settings.DB_HOSTNAME}:{settings.DB_PORT}/{settings.DB_NAME}"
)

engine = create_engine(MYSQL_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
