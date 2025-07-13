from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True, index=True)
    hashed_password = Column(String, nullable=False)

class Travel(Base):
    __tablename__ = "travels"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    fullname = Column(String, nullable=False)
    destination_province = Column(String, nullable=False)
    travel_date = Column(DateTime, nullable=False)
