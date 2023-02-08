from .models import User, Lesson
from .db import session
from logger.logger import logger

def addUser(userInfo) -> User:
    user = User(
        chat_id=userInfo.user.id,
        username=userInfo.user.username,
        first_name=userInfo.user.first_name,
        last_name=userInfo.user.last_name,
        is_messaging=True,
        group_id=1
    )
    try:
        session.add(user)
        session.commit()
    except:
        logger.error(f"user {user} is not valid")


def addLesson(lessonInfo: dict) -> User:
    lesson = Lesson(
        name=lessonInfo['name'],
        link=lessonInfo['link'],
        meeting_id=lessonInfo['meetingId'],
        password=lessonInfo['password_id'],
        teacher=lessonInfo['teacher']
    )
    try:
        session.add(lesson)
        session.commit()
    except:
        logger.error(f"lesson {lesson} is not valid")
