from db.models import createModels
from threading import Thread
from services.bot.bot import bot
from services.bot.handlers import *
from services.lessonsSchedule.scheduleChecker import weekly_schedule_sending
from admin import app 

def main():
    
    Thread(target=(lambda: app.run(port=8080,debug=True, use_reloader=False))).start() 
    
    weekly_schedule_sending()
    
    createModels()
    bot.polling(non_stop=True, allowed_updates=['all'])
    

if __name__ == "__main__":
    main()