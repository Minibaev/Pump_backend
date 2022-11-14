from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
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
    pump_ost = relationship("PumpAggregate", back_populates="ost_pump")


class PumpAggregate(DeclarativeBase):
    __tablename__ = "PumpAggregate"

    id = Column(Integer, primary_key=True)
    station = Column(Integer, nullable=False)
    ost_id = Column(Integer, ForeignKey("OST.id", ondelete="CASCADE"))
    pump = Column(String, nullable=True)
    electric_motor = Column(String, nullable=False)
    kpd_pump = Column(Float, nullable=False)
    kpd_electric = Column(Float, nullable=False)
    ost_pump = relationship("OST", back_populates="pump_ost")
