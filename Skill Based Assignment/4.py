from datetime import datetime 

waktu = datetime.now()

tahun  = waktu.strftime('%Y')

print()
tahun = int(tahun)

print('Tahun ini :',tahun)
print()

pkd = int(input('Populasi kota digital : '))
pkt = int(input('Populasi kota talent : '))
rpd = float(input('rate pertumbuhan kota Digital : '))
rpt = float(input('rate pertumbuhan kota talent : '))


while pkt < pkd :
    pkd = pkd + (pkd * rpd)
    pkt = pkt + (pkt * rpt)
    tahun += 1

print('Tahun : ',tahun)
print('Populasi kota digital : ',pkd)
print('Populasi kota talent : ',pkt)