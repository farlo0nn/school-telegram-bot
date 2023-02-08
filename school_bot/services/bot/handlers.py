from school_bot.services.bot import bot 
from school_bot.db import session
from school_bot.db.models import Lesson
from school_bot.services.bot.utils import changeMessaging, getUserMessagingAndGroupInfo, \
    gen_markup,start, unidentifiedMessage, changeGroup, sendLessonInformation
from school_bot.services.bot.botMessages import LESSONS_MESSAGE, RINGS_MESSAGE, HELP_MESSAGE

@bot.message_handler(content_types=["text"],commands=["start"])
def startHandler(message):
    start(message.chat.id)

@bot.message_handler(content_types=["text"],commands=["help"])
def helpHandler(message):
    bot.send_message(message.chat.id, HELP_MESSAGE) 

@bot.message_handler(content_types=["text"],commands=["lessons"])
def lessonsHelpHandler(message):
    bot.send_message(message.chat.id, LESSONS_MESSAGE) 

@bot.message_handler(commands=["changegroup"])
def changeGroupHandler(message):
    bot.send_message(message.chat.id, "Choose your group:", reply_markup=gen_markup())

@bot.message_handler(commands=["changegroup"])
def changeGroupHandler(message):
    bot.send_message(message.chat.id, "Choose your group:", reply_markup=gen_markup())

@bot.message_handler(commands=["messaging"])
def changeMessagingHandler(message):
    changeMessaging(message.chat.id)

@bot.message_handler(commands=["info"])
def getUserInfoHandler(message):
    getUserMessagingAndGroupInfo(message.chat.id)

@bot.message_handler(commands=["schedule"])
def scheduleSendHandler(message):
    bot.send_photo(message.chat.id,photo=open("static/schedule.jpg","rb"))

@bot.message_handler(commands=["rings"])
def ringsSendHandler(message):
    bot.send_message(message.chat.id,text=RINGS_MESSAGE)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_1":
        changeGroup(call.message.chat.id, 1)
        bot.answer_callback_query(call.id, "you are in a first group")
    elif call.data == "cb_2":
        changeGroup(call.message.chat.id, 2)
        bot.answer_callback_query(call.id, "you are in a second group")


# other commands
@bot.message_handler(content_types=["text"])
def sendInfo(message):
    lesson: Lesson = session.query(Lesson).filter_by(name=message.text.replace('/','')).first()
    if lesson is not None:
        sendLessonInformation(message.chat.id, lesson.name)
    else:
        unidentifiedMessage(message.chat.id)

    


