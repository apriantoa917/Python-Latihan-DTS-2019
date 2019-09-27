# 5.1.2.10 Useful modules | platform

from platform import platform, machine,processor, system,version,python_implementation, python_version_tuple

# platfrom = mengakses data platform yang mendasari ini, yaitu, perangkat keras, sistem operasi, dan informasi versi interpreter.

print(platform())
print(platform(1))
print(platform(0, 1))
print(platform(1, 0))

# machine = mengembalikan generic name prosesor yang menjalankan python 

print(machine())

# processor = nama prosesor yang sebenarnya

print(processor())

# system = mengembalikan nama OS yang digunakan

print(system())

# version = mengembalikan version OS yang digunakan

print(version())

# python implementation = mengembalikan tipe python yang digunakan, secara default mengembalikan cpython kecuali menggunakan tipe lain

print(python_implementation())

# python version tuple = mengembalikan informasi versi dari python yang berisi
    # the major part of Python's version;
    # the minor part;
    # the patch level number.

for atr in python_version_tuple():
    print(atr)

# all module can find in : https://docs.python.org/3/py-modindex.html