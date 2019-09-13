# 4.1.6.1 Tuples and dictionaries

# tuple memiliki konsep sama dengan list, perbedaan mendasar tuple dengan list adalah :
# Tuples
# - tuple menggunakan (), list menggunakan []
# - isi dari tuple tidak dapat dimodifikasi setelah di inisialisasi, tidak dapat ditambah (append) atau hapus (delete)
# - yang dapat dilakukan tuple :
#     - len()
#     - + (tambah), menambah elemen baru di dalam tuple (konsep append di list)
#     - * (multiple), menggandakan isi tuple sejumlah n dengan isi yang sama
#     - in, not in. sama dengan list

myTuple = (1, 10, 100)

t1 = myTuple + (1000, 10000)
t2 = myTuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in myTuple)
print(-10 not in myTuple)