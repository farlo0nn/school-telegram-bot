from school_bot.db.models import createModels
from threading import Thread
from school_bot.services.bot import bot
from school_bot.services.bot.handlers import *
from school_bot.services.lessonsSchedule.scheduleChecker import weekly_schedule_sending
from school_bot.admin import app 

def main():
    
    Thread(target=(lambda: app.run(port=8080,debug=True, use_reloader=False))).start() 
    
    weekly_schedule_sending()
    
    createModels()
    bot.polling(non_stop=True, allowed_updates=['all'])
    

if __name__ == "__main__":
    main()