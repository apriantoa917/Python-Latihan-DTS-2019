# 5.1.5.7 The anatomy of exceptions | assert

# assert : mempertegas pernyataan agar sesuai dengan kondisi yang diminta, kondisi yang tidak sesuai akan menunjukan exception AssertionError
# coba jalankan kode dengan kondisi > 0 dan < 0
# assert berguna untuk validasi data

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)