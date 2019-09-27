# 4.1.6.12 RINGKASAN BAGIAN (3/3)

# assign variabel dengan tuple

tup = (1,2,3)

a, b , c = tup # jumlah var yang di assign harus sama dengan len() tuple

print(a + b + c)


# mencari jumlah data yang duplikat / redundan

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9

duplicates = tup.count(2)

print(duplicates)    # outputs: 4

# menggabungkan 2 dictionary ke dalam dictionary baru /lain menggunakan dict.update()

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# mengubah list menjadi tupple

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)

# mengubah tuple menjadi dictionary

colors = (("green", "#008000"), ("blue", "#0000FF")) # harus berisi 2 value di item tuple

colDict = dict(colors)

print(colDict)

# menyalin dictionary ke dictionary lain

myDict = {"A":1, "B":2}
copyMyDict = myDict.copy()
myDict.clear()

print(copyMyDict)