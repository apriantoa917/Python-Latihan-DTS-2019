# 4.1.6.13 PROJECT: Tic-Tac-Toe
from random import randrange
import time

block = [None,None,None,None,"X",None,None,None,None,]

result = "Draw"

def showBoard():
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', boardValue(1), '  |  ', boardValue(2), '  |  ', boardValue(3), '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', boardValue(4), '  |  ', boardValue(5),'  |  ', boardValue(6), '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', boardValue(7), '  |  ', boardValue(8), '  |  ', boardValue(9), '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def boardValue(num):
    if (block[num-1] == None):
        return num
    return block[num-1]

def userInput():
    print()
    print('Turn : Hooman')
    user = int(input('choose number :'))
    if (block[user-1] == None):
        block[user-1] = "O"
        showBoard()
    else:
        print('kotak yang dipilih sudah terisi')
        userInput()

def compInput():
    comp = randrange(1,10)
    if (block[comp-1] == None):
        block[comp-1] = "X"
        print()
        print('Turn : Computer')
        print('choose number :',comp)
        showBoard()
    else:
        compInput()

def score():
    global result
    if(block[0] == "O" and block[1] == "O" and block[2] == "O" or\
        block[0] == "O" and block[3] == "O" and block[6] == "O" or\
            block[2] == "O" and block[5] == "O" and block[8] == "O" or\
                block[6] == "O" and block[7] == "O" and block[8] == "O"):
        result = "Hooman"
    elif (block[0] == "X" and block[1] == "X" and block[2] == "X" or\
        block[3] == "X" and block[4] == "X" and block[5] == "X" or\
            block[6] == "X" and block[7] == "X" and block[8] == "X" or\
                block[0] == "X" and block[3] == "X" and block[6] == "X" or\
                    block[1] == "X" and block[4] == "X" and block[7] == "X" or\
                        block[2] == "X" and block[5] == "X" and block[8] == "X" or\
                            block[0] == "X" and block[4] == "X" and block[8] == "X" or\
                                block[2] == "X" and block[4] == "X" and block[6] == "X"):
        result = "Computer"
    else:
        result = "Draw"

# computer first
print()
print('Turn : Computer')
print('choose number :',5)
showBoard()

counter = 1
while counter <= 9 and result == "Draw":
    if counter % 2 != 0:
        #computer turn
        if counter != 1:
            time.sleep(1)
            compInput()
    else:
        # hooman turn
        userInput()
    score()
    counter += 1

print()
print('-----WIN :',result,'-----')
print()