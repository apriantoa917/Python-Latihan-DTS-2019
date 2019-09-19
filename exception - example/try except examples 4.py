# 5.1.5.2 The anatomy of exceptions

# source image : https://edube.org/uploads/media/default/0001/01/0ee75473d85349d36925771423976c94c08ddbf1.png

# ZeroDivisionError berada di dalam ArithmethicError, jika exceptions menggunkan class yang lebih general maka cakupan lebih banyak
# lihat hasil di bawah

print('percobaan 1 : ZeroDivisionError')
try:
    y = 1/0
except ZeroDivisionError:
    print('ooooppps')
print()

print('percobaan 2 : ArithmeticError')
try:
    y = 1/0
except ArithmeticError:
    print('ooooppps')

# keduanya bisa menjalankan kode yang ada di dalam exceptions karena kelas ZeroDivisionError berada dalam ArithmeticError