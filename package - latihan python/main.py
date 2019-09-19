import os

print(os.getcwd()) # dir sekarang

os.chdir('D:\\Project\\Project Python\\DTS Python\\package - latihan python')

print(os.getcwd()) # dir setelah ubah dir

import latihan_package.alpha as a

a.alphasatu()
