# 4.1.4.1 Lingkup dalam Python

# scope = pengaksesan var diluar fungsi agar bisa dipakai didalam fungsi

# contoh sederhana : dapat mengakses variabel diluar fungsi

def Scopes():
    print("saya mencetak : ", var)
    
var = "variabel diluar fungsi"
Scopes()
print(var)

print()

# contoh berparameter : nilai dari variabel yang dioperasi didalam fungsi tidak berdampak pada variabel asal kecuali dengan keyword global

def ubah(n):
    print("sebelum diubah :", n)
    n += 1
    print("setelah diubah : ",n)
m = 2
ubah(m)
print("setelah keluar fungsi : ",m)

print()

# contoh menggunakan variabel global (bisa ubah nilai variabel asal didalam fungsi)
def globe():
    global var
    print("didalam fungsi : ",var)
    var += 90

var = 10
globe()
print("setelah fungsi",var)