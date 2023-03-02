import re


from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import validates
from school_bot.db import base, engine 
from school_bot.db.errors import TimeValidationError
from school_bot.logger import logger

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


class LessonStartTime(base):
    __tablename__ = 'lessonstarttime'
    id = Column(Integer, primary_key=True)
    start_time = Column(String, unique=True)
    
    @validates('start_time')
    def startTimeValidator(self, key, start_time):
        if not isinstance(start_time, str):
            return False
        try:
            splittedTime = re.split(', |\/|:', start_time)
            if len(splittedTime) != 2:
                raise TimeValidationError
            hours, minutes = splittedTime
            if self.valid(hours) and self.valid(minutes):
                hours,minutes = int(hours), int(minutes)
            else:
                raise TimeValidationError
            if 0<=hours<=23 and 0<=minutes<=59:
                return True
        except TimeValidationError:
            logger.error("invalid start time data")
            return False

    @staticmethod
    def valid(variable):
        try: 
            variable = int(variable)
            return True
        except ValueError:
            return False

class WeekDay(base):
    __tablename__ = 'weekday'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Schedule(base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    day_name = Column(String, unique=False, nullable=True)
    lesson_time = Column()

def createModels():
    base.metadata.create_all(engine)