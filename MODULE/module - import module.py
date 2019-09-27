# 5.1.1.7 Importing a module | math

import math # import entitas yang digunakan dalam kode

# cetak hasil sin(pi / 2) --> sin 90 = 1.0

res = math.sin(math.pi/2)

print(res)

# perbedaan pi local var dengan pi module

pi = 3.14 # local var

def sin(x):
    if x * 2 == pi :
        return 0.99999999
    else:
        return None

# test pi local variabel
print('local    ->',sin(pi/2))

# test pi module
print('module   ->',math.sin(math.pi/2))