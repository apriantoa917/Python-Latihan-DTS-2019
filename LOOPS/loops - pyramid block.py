# 3.1.2.14 LAB: Essentials of the while loop

blocks = int(input("Enter the number of blocks: "))

height = 0

layer = 1

while layer <= blocks:          
    blocks = blocks - layer #jumlah blok yang disusun pada setiap layer , 1,2,3...
    height += 1             #bertambah sesuai pertambahan layer
    layer += 1
    

print("The height of the pyramid:", height)