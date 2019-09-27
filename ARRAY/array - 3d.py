# 3.1.7.5 Lists in advanced applications | Arrays

# 3D : merubah nomor kamar yang ada saat dipesan

# kasus : hotel 2 gedung, 2 lantai, 3 ruangan (setiap lantai 3 ruangan)

# mengisi ketersediaan ruangan yang dipesan menjadi kosong 

kamar = [[["kosong" for i in range(3)] for i in range(2)] for i in range(2)]

print(kamar)

# memesan ruang di gedung 1 lantai 2 ruang 3, status ruang jadi False

kamar[0][1][2] = "dipesan" # gedung 1 = index 0, lantai 2 = index 1, ruang 3 = index 2

print(kamar)