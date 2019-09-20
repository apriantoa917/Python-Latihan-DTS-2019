# 5.1.8.9 The nature of strings in Python

alphabet = "abcdefghijklmnopqrstuvwxyz"

# del alphabet[0]

# alphabet.append("A")

# alphabet.insert(0, "A")

# alphabet = String yang dapat dioperasikan namun tidak dapat dilakukan penambahan, pengurangan / penghapusan dengan metode list

#Namun dapat diakali dengan concatenation / penggabungan sebuah string dengan string yang lain

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)