from sqlalchemy import Column, Integer, String, Boolean
from .db import base, engine 

class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, unique = True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_messaging = Column(Boolean, default=1)
    group_id = Column(Integer, default=1)

    def __repr__(self) -> str:
        return f"<User: {self.username}>"

class Lesson(base):
    __tablename__ = 'lesson'
    id = Column(Integer,primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    link = Column(String(255), nullable=False)
    meeting_id = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    teacher = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Lesson: {self.name}>"

def createModels():
    base.metadata.create_all(engine)