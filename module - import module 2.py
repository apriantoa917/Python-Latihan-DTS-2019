# 5.1.1.7 Importing a module | math - 5.1.1.12 Importing a module | aliasing

from math import sin,pi # import entities spesific, hanya sin dan pi. nama variabel yang sama akan menggantikan isi entitas

# print(pi) -> 3.141592653589793
# pi = 2
# print(pi) -> 2

print(sin(pi/2))

import math as moduls # give alias name

from math import pi as PI, sin as sinus

print (PI)

print(sinus(90))

print(moduls.pi)

# from math import * -> import all entities inside module, warning about unused item

# show all entities inside module using dir()

print(dir(moduls))