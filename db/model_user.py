from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    nickname = Column(String)
    email = Column(String)
    addresses = relationship("OST", back_populates="user")


class OST(DeclarativeBase):
    __tablename__ = "OST"

    ost_id = Column(Integer)
    neft_upr = Column(String)
    ost = Column(String)
    user = relationship("User", back_populates="ost")