# 3.1.4.10 Lists - collections of data | lists and loops

#   CARA 1
# menjumlahkan nilai dari semua isi list

myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)

#   CARA 2

myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)