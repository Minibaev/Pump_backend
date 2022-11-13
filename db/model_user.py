from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

DeclarativeBase = declarative_base()


class User(DeclarativeBase):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ost_id = Column(Integer, ForeignKey("OST.id"), nullable=False)
    addresses = relationship("OST", back_populates="user")


class OST(DeclarativeBase):
    __tablename__ = "OST"

    id = Column(Integer, primary_key=True, nullable=False)
    neft_upr = Column(String, nullable=False)
    ost = Column(String, nullable=False)
    user = relationship("User", back_populates="addresses")