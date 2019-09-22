# 5.1.9.10 String methods

name = '   aprianto   '

print(name)
print(name.lstrip())
print(name.lstrip(' a'))

name = 'asc.def,,,ds'
print(name.lstrip('.sacdef'))

print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org"))