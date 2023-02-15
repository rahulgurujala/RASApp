import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

from .crud import crud

Base = declarative_base()


class BaseModel(Base, crud):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
