# 5.1.9.10 String methods, # 5.1.9.13 String methods

# lstrip = menghapus spasi / karakter yang cocok dari kiri (left) hingga karakter tidak ada yang cocok


name = '   aprianto   '

print('['+name+']')
print('['+name.lstrip()+']')
print(name.lstrip(' a'))

name = 'asc.def,,,ds'
print(name.lstrip('.sacdef'))

print("www.cisco.com".lstrip("w.c"))

print("pythoninstitute.org".lstrip(".org"))

# rstrip = menghapus spasi / karakter yang cocok dari kanan (right)
name = '   aprianto   '
print('['+name.rstrip()+']')
print("www.cisco.com".rstrip("om"))
print("www.cisco.com".rstrip(".com"))

#strip() = menghapus spasi / karakter diantara 2 sisi (kanan & kiri)

print("[" + "   aleph   ".strip() + "]")
print("[" + "ooovovooo".strip('o') + "]")
print("[" + "---ovo---".strip('-') + "]")