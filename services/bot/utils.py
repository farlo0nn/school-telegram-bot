from telebot import types
from db.models import User, Lesson
from db.db import session
from db.utils import addUser
from logger.logger import logger
from .bot import bot


def getUserInfoByChatId(id) -> types.ChatMemberMember:
    return bot.get_chat_member(chat_id=id,user_id=id)

def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("1", callback_data="cb_1"),
                               types.InlineKeyboardButton("2", callback_data="cb_2"))
    return markup


def start(chatId):
    userIsPresent = True if session.query(User).filter_by(chat_id=chatId).first() else False
    logger.debug(userIsPresent)
    if not userIsPresent:
        userInfo = getUserInfoByChatId(chatId)
        addUser(userInfo)
    bot.send_message(chatId, "To see all available features type /help\nTo select your group type /changegroup")
    
def changeMessaging(chatId):
    user: User = session.query(User).filter_by(chat_id=chatId).first()
    response = "Messaging stopped" if user.is_messaging else "Messaging resumed"
    user.is_messaging = not user.is_messaging
    try:
        session.add(user)
        session.commit()
    except Exception as ex:
        logger.error(ex)
        bot.send_message("Error occurred")
    bot.send_message(chatId, response)

def changeGroup(chatId, groupId):
    user: User = session.query(User).filter_by(chat_id=chatId).first()
    user.group_id = groupId
    logger.debug(user.group_id)
    session.commit()

def getUserMessagingAndGroupInfo(chatId):
    user: User = session.query(User).filter_by(chat_id=chatId).first()
    messaging = "working" if user.is_messaging else "stopped"
    bot.send_message(chatId, f"Messaging: {messaging}\nYour group: {user.group_id}")
    
def unidentifiedMessage(chatId):
    return bot.send_message(chatId, "Sorry, unidentified command\nPlease try again...")

def sendLessonInformation(chatId, lessonName: str):
    lesson: Lesson = session.query(Lesson).filter_by(name=lessonName).first() 
    response = \
    f"""Lesson: {lesson.name}\nTeacher: {lesson.teacher}\n\n\nMeeting identification code: {lesson.meeting_id}\nMeeting password: {lesson.password}\nLink to zoom meeting: {lesson.link}"""
    bot.send_message(chatId, response)
