# 3.1.4.9 Lists - collections of data | list methods

# membuat list kosong 

a = []

print("isi list sebelum : ",a)

# mengisi list dengan for

for i in range(10):
    a.append(i+1)

print("isi list sesudah : ",a)

# mengisi dengan kebalikannya / reverse

b = []

print("isi list sebelum : ",b)

for i in range(10):
    b.insert(0,i+1)

print("isi list sesudah : ",b)
