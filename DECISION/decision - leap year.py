#3.1.1.13 LAB: Essentials of the if-elif-else statement

year = int(input("Enter a year: "))

if year >= 1582 and year % 4 != 0 :
    print("Common year")
elif year >= 1582 and year % 4 == 0 :
    print("Leap year")
else :
    print("Not within the Gregorian calendar")
    