# 4.1.3.7 LAB: How many days: writing and using your own functions

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
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # <- days[1]  different with module
    res = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 28 # <- different with module
    return res


testyears = [1900, 2000, 2016, 1987, 2001]
testmonths = [2, 2, 1, 11, 2]
testresults = [28, 29, 31, 30, 28]
for i in range(len(testyears)):
    yr = testyears[i]
    mo = testmonths[i]
    print(yr, mo, "-> ", end="")
    result = daysInMonth(yr, mo)
    if result == testresults[i]:
        print("OK")
    else:
        print("Failed")
