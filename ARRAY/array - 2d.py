# 3.1.7.2 Lists in advanced applications | Arrays

# contoh sederhana 

List = []

a = [0,1,2]

b = [3,4,5]

List.append(a)

List.append(b)

print("Bentuk array 2d : ",List)

# dengan looping 

board = []

for i in range(5):
    row = [i for i in range(3)]
    board.append(row)

print(board)

# dengan looping bentuk sederhana

board = [[i for i in range(3)] for i in range(5)]

print(board)
