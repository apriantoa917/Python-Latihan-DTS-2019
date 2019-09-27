# 3.1.6.7 Lists - more details

myList = [17, 3, 11, 5, 1, 9, 78, 15, 13]
largest = myList[0]

for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]

print(largest)