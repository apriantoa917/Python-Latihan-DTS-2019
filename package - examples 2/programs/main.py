# 5.1.3.5 Modules and Packages

from sys import path

for i in range(len(path)):
    print(path[i])

path.insert(0,'D:\\Project\\Project Python\\DTS Python\\package - examples 2\\modules')
print()
for i in range(len(path)):
    print(path[i])

# can you solve this problems below? idk why it can happens
# import module