# gpj = gaji / jam
gpj = int(input('Gaji per jam yang anda inginkan : '))

# jk = jam kerja / minggu
jk = int(input('Jumlah jam kerja yang akan dilakukan dalam 1 minggu : '))

# gpm = gaji per minggu
gpm = gpj * jk

# tg = total gaji
tg = gpm * 5
print('Total Gaji sebelum Pajak :',tg)

# tgp = total gaji setelah pajak, pjk = pajak = 14%
pjk = (14/100) * tg
tgp = tg - pjk
print('Total Gaji setelah pajak :',tgp)

# ba = 10% baju & aksesoris
ba = (10/100) * tgp
print('Biaya untuk Baju dan Aksesoris :',ba)

# atk = 1% alat tulis
atk = (1/100) * tgp
print('Biaya untuk Alat tulis :',atk)

sisa = tgp - (ba + atk)

# sdk = 25% sisa untuk sedekah
sdk = (25/100) * sisa
print('Jumlah uang disedekahkan :',sdk)

# ay = 30% sedekah untuk anak yatim
ay = (30/100) * sdk
print('Jumlah yang diterima anak yatim :',ay)

# kd = sisa sedekah - 30 % untuk kaum dhuafa
kd = sdk - ay
print('Jumlah yang diterima kaum dhuafa :',kd)