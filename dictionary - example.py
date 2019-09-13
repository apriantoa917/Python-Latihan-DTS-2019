#  4.1.6.4 Tuples and dictionaries

# dictionary -> sebuah pasangan key - value yang disimpan dalam suatu list dictionary
# - key harus unique
# - key dapat berupa tipe data apapun
# - bisa memakai fungsi len()
# - satu arah, hanya bisa mencari dengan key untuk menemukan value, tidak bisa sebaliknya


dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dict:    
        print(word, "->", dict[word])
    else:
        print(word, "is not in dictionary")

print(dict)