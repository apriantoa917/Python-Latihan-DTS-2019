# 3.1.5.2 Sorting simple lists - the bubble sort algorithm
# 3.1.5.3 Sorting simple lists - the bubble sort algorithm

# cara sendiri

myList = [8, 10, 6, 2, 4]

n = len(myList)

i = 0   # inisialisasi index

while i < n : # looping sebanyak jumlah index - 1 (perulangan vertikal) & i sebagai angka pembanding 1
    j = i + 1 # inisialisasi j sebagai angka pembanding 2
    while j < n : #looping horizontal
        if myList[j] < myList [i] :
            myList[i], myList[j] =  myList[j], myList[i] #swapping
        j+= 1
    i+=1
print(myList)

# cara python -------------------------------------------------------------------------------

myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)

# cara python very simple -------------------------------------------------------------------

# menggunakan method sort()

myList = [8, 10, 6, 2, 4] # list to sort

myList.sort()

print(myList)