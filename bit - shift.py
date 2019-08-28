# 3.1.3.5 Logic and bit operations in Python | Bit shifting

#fungsi untuk mengembalikan nilai biner , src : stack overflow

def castBin(biner):
    print(('0' * 7 + bin(biner)[2:])[-8:])

# digunakan untuk menggeser nilai bit / biner dari integer ke kanan / kiri

# dilambangkan dengan << untuk shift kiri dan >> untuk shift kanan

var = 10

leftVar = var << 1 # menggeser nilai biner dari var ke kiri sebanyak 1 kali

rightVar = var >> 1 # menggeser nilai biner dari var ke kanan sebanyak 1 kali

castBin(var) #biner 10
castBin(leftVar) #biner shift left 1 dari 10
castBin(rightVar) #biner shift right 1 dari 10
