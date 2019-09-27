# 3.1.4.6 LAB: The basics of lists

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

indices = int(input("enter a new number : "))

hatList[2] = indices

del hatList[4]

print(len(hatList))

print(hatList)