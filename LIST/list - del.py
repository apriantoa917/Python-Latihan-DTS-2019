# 3.1.6.5 Operations on lists | slices, del

a = [0,1,2,3,4,5]

# delete semua elemen list

del a[:] # cara 1

print(a)

a = [0,1,2,3,4,5]

# cara 2

# del a -------------> jika ini aktif print a akan eror, list jadi hilang

# print(a)

# delete sebagian / bagian tertentu

a = [0,1,2,3,4,5]

del a[0:3] # hapus elemen index 0,1,2

print(a)

