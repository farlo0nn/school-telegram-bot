from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from school_bot.config import SQLITE_DB_FILE

base = declarative_base()
engine = create_engine(f"sqlite:///{SQLITE_DB_FILE}",connect_args={"check_same_thread": False})
base.metadata.bind = engine
session = sessionmaker(bind=engine)()