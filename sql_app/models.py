from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,DateTime
from sqlalchemy_utils import EmailType
import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    email = Column(EmailType)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)