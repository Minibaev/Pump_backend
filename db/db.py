from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.model_user import DeclarativeBase


engine = create_engine('sqlite:///test.db')
DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
