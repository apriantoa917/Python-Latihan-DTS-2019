# 5.1.11.1 Four simple programs

text = input('Masukan text : ')
hasil=''
for abjad in text:
    if not abjad.isalpha(): # mengecek apakah karakter bukan berupa abjad
        hasil += abjad
    else:
        encrypt = ord(abjad.upper())
        encrypt += 1
        if encrypt > ord('Z'):
            encrypt = ord('A')
        hasil += chr(encrypt)
print(hasil)