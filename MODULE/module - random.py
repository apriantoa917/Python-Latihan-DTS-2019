# 5.1.2.6 Useful modules | random - 5.1.2.9 Useful modules | random

from random import random, seed, randrange, randint

seed(0)

# generally random :

for i in range(5):
    print('random           :',random())

# randrange
for i in range(5):
    print('randrange        :',randrange(1,5))

for i in range(5):
    print('randrange plus   :',randrange(1,5+3))

for i in range(5):    
    print('randrange step   :',randrange(1,16,4))

# randint
for i in range(5):
    print('randint          :',randint(0,7))

lst = [randint(1,20) for i in range(10)]

print(lst)

for i in range(len(lst)):
    print(lst[randint(0,len(lst)-1)])