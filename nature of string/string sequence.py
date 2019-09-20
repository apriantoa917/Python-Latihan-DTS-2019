# 5.1.8.6 The nature of strings in Python

# indexing : memerankan string sebagai elemen index yang dapat diakses

str1 = 'sebuah kata'

for i in range(len(str1)):
    print(str1[i],end=' ')
print()


#iterating : memanggil string berdasarkan urutannya 

for str2 in str1:
    print(str2,end=' ')