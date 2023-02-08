import schedule


from threading import Thread
from time import sleep
from school_bot.services.lessonsSchedule.weeklySchedule import WeeklySchedule

def weekly_schedule_sending(testMode=None):
    weekly_schedule = WeeklySchedule(testMode=testMode)
    weekly_schedule.whole_schedule()
    Thread(target=schedule_checker).start() 

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(2)