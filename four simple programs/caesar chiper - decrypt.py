# 5.1.11.2 Four simple programs

text = input('Masukan text : ')
hasil=''
for abjad in text:
    if not abjad.isalpha(): # mengecek apakah karakter bukan berupa abjad
        hasil += abjad
    else:
        decrypt = ord(abjad.upper())
        decrypt -= 1
        if decrypt < ord('A'):
            decrypt = ord('Z')
        hasil += chr(decrypt)
print(hasil)