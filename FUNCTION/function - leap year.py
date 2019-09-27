# 4.1.3.6 LAB: A leap year: writing your own functions


def isYearLeap(year):
    if year >= 1582 :
        if year % 4 == 0 :
            return True
        else :
            return False
    else :
        return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
