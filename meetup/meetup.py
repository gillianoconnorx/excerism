from datetime import date
from calendar import Calendar

class MeetupDayException(BaseException):
    def __init__ (self, message):
        self.message = message

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cal = Calendar()

def meetup_day(year, month, dow, which):
    day = days_of_week.index(days_of_week)
    candidates = ([day for day, day_of_week in cal.itermonthdays2(2018, 12)
    if day!=0 and day == day])
    if which == 'last':
        meetup_day = candidates[-1]
    elif which == 'teenth':
        meetup_day = [day for day in candidates if day >= 13][0]
    else:
        ordinal = int(which[0])
        if ordinal > len(candidates):
            raise MeetupDayException("no such day in month")
        else:
            meetup_day = candidates[ordinal -1]
    return date(year, month, meetup_day)    
    




