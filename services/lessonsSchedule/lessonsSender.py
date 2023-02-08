import json

from loguru import logger
from services.bot.bot import bot
from db.db import session
from db.models import User, Lesson
from sqlalchemy.orm.query import Query
from logger.logger import logger
from settings import SAD_STICKER_ID


class LessonsSender:

    def __init__(self) -> None:
        self.currentLessons: dict = {}
        self.curLesson: Lesson = None

    def setLesson(self, lessonNameGroupsDict: dict ):
        for lessonName in lessonNameGroupsDict.keys():
            for groupId in lessonNameGroupsDict[lessonName]:
                self.currentLessons[groupId] = lessonName
        self._sendMeetingLink()

    def _sendMeetingLink(self) -> None:
        users: list[User] = session.query(User).filter_by(is_messaging=1).all()
        # logger.debug(''.join(''.join(chat_ids)))
        for user in users:
            self.curLesson: Lesson = session.query(Lesson).filter_by(name=self.currentLessons[user.group_id]).first()
            
            if self.curLesson is None:
                response = f"Current lesson is \"{self.currentLessons[user.group_id]}\", but we have no information about it"
                bot.send_message(user.chat_id, response)
                bot.send_sticker(user.chat_id, sticker=SAD_STICKER_ID)
                
                return 
            else:
                response = \
                f"""Lesson: {self.curLesson.name}\nTeacher: {self.curLesson.teacher}\n\n\nMeeting identification code: {self.curLesson.meeting_id}\nMeeting password: {self.curLesson.password}\nLink to zoom meeting: {self.curLesson.link}"""
                self._sendMessage(user,response)
        return 

    def _sendMessage(self,user: User, response):
        try:
            bot.send_message(user.chat_id, response)
            logger.success(f"chat_id: {user.username}, group: {user.group_id}, lesson: {self.curLesson.name}")
        except Exception as ex:
            logger.error(ex)
            # deleteUser(chat_id)
