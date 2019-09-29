# 6.1.4.6 OOP: Methods

# digunakan mengambil nama file dari class / obj yang sedang aktif
# Atribut __name__ tidak ada dari objek - atribut hanya ada di dalam kelas.
# Jika ingin menggunakan __name__, gunakan type(obj) untuk mengambil kelas yang digunakan instance

class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

# 6.1.4.7 OOP: Methods

# sama seperti __name__, module digunakan untuk mnegambil nama module yang sedang aktif digunakan dalam class / instance obj

print(Classy.__module__)
obj = Classy()
print(obj.__module__)

# 6.1.4.8 OOP: Methods

# bases adalah tuples yang mengembalikan nama superclass yang sedang digunakan oleh class / sub class 

class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)