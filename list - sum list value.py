# 3.1.4.10 Lists - collections of data | lists and loops

# menjumlahkan nilai dari semua isi list

myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)