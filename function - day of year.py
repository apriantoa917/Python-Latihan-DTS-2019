#4.1.3.8 LAB: Day of the year: writing and using your own functions

def isYearLeap(year):
    if year >= 1582:
        if year % 4 == 0:
            return True
        else:
            return False
    else:
        return False


def daysInMonth(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 28 # <-- should be 28, prev in skeleton written 29
    return res

def dayOfYear(year, month, day):
    days = 0
    for m in range (1,month):
        days+= daysInMonth(year,m)
    return days

print(dayOfYear(2000, 12, 31))