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
    else:
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isYearLeap(year):
            days[1] = 28
        return days[month-1]

day = 0
for i in range(1,13):
    day += daysInMonth(2002,i)

print("day of year", day)