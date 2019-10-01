mapel = { '001':'Bahasa Indonesia', '002':'Bahasa Inggris', '003':'Matematika', '004':'Biologi', '005':'Fisika'}

for i in range(5):
    kode = input('Masukan kode Mapel : ')
    nama = input('Masukan Nama Mapel : ')
    mapel[kode] = nama
    print()

mapel['003'] = 'Kimia'
mapel['005'] = 'Olahraga'

for kode in sorted(mapel.keys()):
    print(kode,'==>',mapel[kode])