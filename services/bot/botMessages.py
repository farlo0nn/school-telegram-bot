from db.db import session
from db.models import Lesson

__backslash_n = '\n'

HELP_MESSAGE = \
"""
Welcome to zoom_links_bot
This bot is designed for quick access to tutorial links, conference codes and passwords
You can get information on the subject of interest by writing its name in chat
To stop/resume sending links at the conference before lessons, write the command:
/messaging
If you want to check your group or check if you receive information write a command:
/info
To get weekly schedule write command:
/schedule
To get rings schedule write command:
/rings
To change your group write command:
/changegroup
To get information about getting information about specific lesson write:
/lessons
"""

LESSONS_MESSAGE = \
f"""
You can receive information about specific lesson, to do it, please type or press this commands:
{__backslash_n.join([f"{lesson.name.capitalize()} - /{lesson.name}" for lesson in session.query(Lesson).all()])}
"""

RINGS_MESSAGE = \
f"""
0..Zero Lesson | 8:40 - 9:00
1..First Lesson | 9:05 - 9:50
2..Second Lesson | 10:00 - 10:45
3..Third Lesson | 10:55 - 11:40
4..Fourth Lesson | 11:50 - 12:35
5..Fifth Lesson | 13:05 - 13:50
6..Sixth Lesson | 14:00 - 14:45
7..Seventh Lesson | 14:55 - 15:50
8..Eighth Lesson | 15:55 - 16:40
"""