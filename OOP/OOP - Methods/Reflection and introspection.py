# 6.1.4.9 OOP: Methods

# introspeksi, yang merupakan kemampuan suatu program untuk memeriksa jenis atau properti suatu objek pada saat runtime;
# refleksi, yang melangkah lebih jauh, dan merupakan kemampuan program untuk memanipulasi nilai, properti, dan / atau fungsi suatu objek saat runtime.


# 6.1.4.10 OOP: Methods

class MyClass:
    pass

# Refleksi dan introspeksi memungkinkan seorang programmer untuk melakukan apa saja dengan setiap objek, tidak peduli dari mana asalnya. 

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj): # function untuk menambah 1 untuk tipe variabel integer yang diawali dengan huruf i
    for name in obj.__dict__.keys():    # looping setiap key di dictionary
        if name.startswith('i'):        # seleksi variabel yang diawali huruf i
            val = getattr(obj, name)    # mengambil nilai dari var itu
            if isinstance(val, int):    # seleksi tipe data untuk integer
                setattr(obj, name, val + 1) # jika int tambah 1

print(obj.__dict__) # cetak semua dict setelah invoke
incIntsI(obj)       # jalankan function
print(obj.__dict__) # cetak semua dict setelah function