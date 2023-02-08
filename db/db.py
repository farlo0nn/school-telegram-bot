import sqlalchemy.orm as orm


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

base = declarative_base()
engine = create_engine("sqlite:///db.sqlite",connect_args={"check_same_thread": False})
base.metadata.bind = engine
session = sessionmaker(bind=engine)()