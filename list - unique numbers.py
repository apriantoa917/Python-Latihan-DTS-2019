# 3.1.6.9 LAB: Operating with lists - basics

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

dumpList = []

for i in myList :
    if i not in dumpList :
        dumpList.append(i)

myList = dumpList

print(myList)