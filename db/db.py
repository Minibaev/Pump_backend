from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.model_user import DeclarativeBase
from db.get_path import get_db_url


engine = create_engine(get_db_url())
DeclarativeBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
