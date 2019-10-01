from datetime import datetime 

waktu = datetime.now()

def crJam():
    return waktu.strftime('%H')

def crMin():
    return waktu.strftime('%M')

print('JAM SERVER : ',crJam(),':',crMin())

tipe = 1
jm = 0
mm = 0
total = 0

def masuk():
    try:
        global jm,mm,tipe
        tipe = int(input('Tipe kendaraan : 1. Mobil    2. Motor\n>>>'))
        if tipe == 1 or tipe == 2:
            cek = True
        if not cek:
            print('Tipe kendaraan harus valid')
            masuk()
        
        jm = int(input('Masukan Waktu Parkir (Jam)      : '))
        mm = int(input('Masukan Waktu Parkir (Menit)    : '))
        if jm < 0 or jm > 59 or mm < 0 or mm > 59:
            print('Masukan jam / menit yang valid')
            masuk()
        
        
    except:
        print('!!! inputan harus berupa angka !!!')
        masuk()
    

denda = False

masuk()

jk = int(crJam())
mk = int (crMin())

lpm = mk - mm
lpj = jk - jm

if lpm < 0:
    mk += 60
    jk -= 1
    lpm = mk - mm
    lpj = jk - jm

if jk < jm:
    denda = True

if mk > 59:
    mk -= 60
    jk += 1

print('jam masuk                -> ',jm,':',mm)
print('jam keluar               -> ',jk,':',mk)

if not denda:
    print('Lama parkir              -> ',lpj,':',lpm)

    if lpm > 0: # jika lama parkir menit > 0 maka dibulatkan jadi jam selanjutnya
        lpm = 0
        lpj += 1

    print('Pembulatan Lama Parkir   ->',lpj,'jam')
    next = 0
    if tipe == 1:
        next = 4000
    elif tipe == 2:
        next = 2000

    if lpj <= 2:
        total = 2000
    else :
        total = 2000
        lpj -= 2
        total = total + (lpj * next)
else :
    print('Anda terkena denda')
    total = 100000

print('TOTAL BIAYA : Rp',total)




