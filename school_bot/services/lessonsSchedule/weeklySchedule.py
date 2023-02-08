import schedule
from school_bot.services.lessonsSchedule.lessonsSender import LessonsSender

class WeeklySchedule():

    def __init__(self, testMode=None) -> None:
        self.testMode = testMode
        self.sender = LessonsSender()

        self.monday = {
            "firstLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "secondLesson": (lambda: self.sender.setLesson({
                "ukranian": [1,2]
            })),
            "thirdLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "fourthLesson": (lambda: self.sender.setLesson({
                "biology": [1,2],
                "chemistry": [1,2]
            })),
            "fifthLesson": (lambda: self.sender.setLesson({
                "physics": [1,2]
            })),
            "sixthLesson": (lambda: self.sender.setLesson({
                "literature": [1,2]
            })),
            "seventhLesson": (lambda: self.sender.setLesson({
                "it": [1,2]
            })),
        }

        self.tuesday = {
            "firstLesson": (lambda: self.sender.setLesson({
                "english": [1,2]
            })),
            "secondLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "thirdLesson": (lambda: self.sender.setLesson({
                "physics": [1,2]
            })),
            "fourthLesson": (lambda: self.sender.setLesson({
                "chemistry": [1,2]
            })),
            "fifthLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "sixthLesson": (lambda: self.sender.setLesson({
                "physics": [1,2]
            })),
            "seventhLesson": (lambda: self.sender.setLesson({
                "history": [1,2]
            })),
        }

        self.wednesday = {
            "firstLesson": (lambda: self.sender.setLesson({
                "defending": [1,2]
            })),
            "secondLesson": (lambda: self.sender.setLesson({
                "civilEducation": [1,2]
            })),
            "thirdLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "fourthLesson": (lambda: self.sender.setLesson({
                "pe": [1,2]
            })),
            "fifthLesson": (lambda: self.sender.setLesson({
                "math": [2],
                "physics": [1]
            })),
            "sixthLesson": (lambda: self.sender.setLesson({
                "math": [1],
                "physics": [2]
            })),
            "seventhLesson": (lambda: self.sender.setLesson({
                "civilEducation": [1,2],
                "defending": [1,2]
            })),
        }

        self.thursday = {
            "firstLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "secondLesson": (lambda: self.sender.setLesson({
                "geography": [1,2]
            })),
            "thirdLesson": (lambda: self.sender.setLesson({
                "math": [1,2]
            })),
            "fourthLesson": (lambda: self.sender.setLesson({
                "physics": [1,2]
            })),
            "fifthLesson": (lambda: self.sender.setLesson({
                "ukranian": [1,2]
            })),
            "sixthLesson": (lambda: self.sender.setLesson({
                "biology": [1,2]
            })),
            "seventhLesson": (lambda: self.sender.setLesson({
                "history": [1,2]
            })),
            "eighthLesson": (lambda: self.sender.setLesson({
                "pe": [1,2]
            })),
        }

        self.friday = {
            "firstLesson": (lambda: self.sender.setLesson({
                "ukranian": [1,2]
            })),
            "secondLesson": (lambda: self.sender.setLesson({
                "ukranian": [1],
                "physics": [2]
            })),
            "thirdLesson": (lambda: self.sender.setLesson({
                "ukranian": [2],
                "physics": [1]
            })),
            "fourthLesson": (lambda: self.sender.setLesson({
                "pe": [1,2]
            })),
            "fifthLesson": (lambda: self.sender.setLesson({
                "it": [1,2]
            })),
            "sixthLesson": (lambda: self.sender.setLesson({
                "english": [1],
                "math": [2]
            })),
            "seventhLesson": (lambda: self.sender.setLesson({
                "english": [2],
                "math": [1]
            })),
        }

        self.lessonsTime = {
            "zeroLesson": "08:38",
            "firstLesson": "09:03",
            "secondLesson": "09:58",
            "thirdLesson": "10:53",
            "fourthLesson": "11:48",
            "fifthLesson": "13:03",
            "sixthLesson": "13:58",
            "seventhLesson": "14:53",
            "eighthLesson" : "15:43",
        }

    def test(self):
        schedule.every(10).seconds.do(self.monday["firstLesson"])

    def monday_schedule(self):
        for lesson in self.monday.keys():
            schedule.every().monday.at(self.lessonsTime[f"{lesson}"]).do(self.monday[f"{lesson}"])

    def tuesday_schedule(self):
        for lesson in self.tuesday.keys():
            schedule.every().tuesday.at(self.lessonsTime[f"{lesson}"]).do(self.tuesday[f"{lesson}"])
        

    def wednesday_schedule(self):        
        for lesson in self.wednesday.keys():
            schedule.every().wednesday.at(self.lessonsTime[f"{lesson}"]).do(self.wednesday[f"{lesson}"])
            
    def thursday_schedule(self):
        for lesson in self.thursday.keys():
            schedule.every().thursday.at(self.lessonsTime[f"{lesson}"]).do(self.thursday[f"{lesson}"])

    def friday_schedule(self):
        for lesson in self.friday.keys():
            schedule.every().friday.at(self.lessonsTime[f"{lesson}"]).do(self.friday[f"{lesson}"])



    def whole_schedule(self):
        self.monday_schedule()
        self.tuesday_schedule()
        self.wednesday_schedule()
        self.thursday_schedule()
        self.friday_schedule()
        if self.testMode is not None:
            self.test()