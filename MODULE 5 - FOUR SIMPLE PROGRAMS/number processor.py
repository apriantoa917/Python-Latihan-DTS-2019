# 5.1.11.3 Four simple programs

inputs = input('Masukan deret angka yang akan ditotal : ')
data = inputs.split()
if len(data) == 0:
    print(' tidak ada data yang diinput')
else:
    total = 0
    try:
        for item in data:
            total += float(item)
    except:
        print(item,'bukan angka')
    print(total)