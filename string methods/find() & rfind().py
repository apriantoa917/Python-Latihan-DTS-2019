# 5.1.9.4 String methods, 5.1.9.12 String methods

# find mengembalikan index dimana karakter yang dicari dalam sebuah kata berada
# find seperti index tapi lebih aman. find tidak menyebabkan eror saat karakter yang dicari dari sebuah kata tidak ada, hanya mengembalikan -1
# find hanya bekerja pada string saja

print('akuuuuu'.find('u')) # kata u ada di index ke 2 (uuu setelah index 2 tidak terhitung)
print('akuuuuu'.find('e')) # kata e tidak ada, mengembalikan nilai -1
print()


txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)
print()

# find juga memiliki fitur pembatasan index pencarian dengan 3 parameter yaitu (kata yang dicari | index awal mulai | 1 < batas akhir)

kata = 'hahe'

print(kata.find('a',0,3)) # kata yang dicari = a dimulai dari index 0 (h) sampai index ke 2 (3-1 = 2 = h), ditemukan : ya, index = 1
print(kata.find('a',0,1)) # kata yang dicari = a dimulai dari index 0 (h) sampai index ke 0 (1-1 = 0 = h), ditemukan : tidak, index = -1

print()
print("rfind")
print()

# rfind = right find = kebalikan find(). jika find mengembalikan indeks karakter yang cocok di awal (index pertama yang cocok), rfind mengembalikan index karakter yang cocok pada akhir
# misal : kata = abcdefcabcd , find(c) , index = 2, c yang cocok pertama ada di index ke 2
#                            rfind(c), index = 9, c yang cocok terakhir ada di index ke 9(paling kanan/akhir)

# Demonstrating the rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9)) # meski sebelumnya ta sudah ketemu 2*, index awal 0 - 9 (berhenti di t) pencarian dilakukan dari kiri ke kanan, hanya menemukan t bukan ta
print("tau tau tau".rfind("ta", 3, 9))