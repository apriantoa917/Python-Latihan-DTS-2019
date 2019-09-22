# 5.1.10.3 String in action

# untuk sorting ada 2 cara yang bisa dilakukan, menggunakan sorted() dan sort()

# sorted() dijalankan dengan memanggil fungsinya dan diisi parameter berupa list

lst = ['omega', 'alpha', 'pi', 'gamma']

print('list original',lst)
sorted(lst) # tidak akan berdampak karena hanya dapat digunakan untuk ditampung di list lain / langsung di print
print('list setelah dipanggil methodnya',lst)
print('list yang dipanggil methodnya langsung di print',sorted(lst))
lstnew = sorted(lst)
print('list baru yang menampung nilai list yang dipanggil methodnya',lstnew)

# metode kedua dengan sort() dengan memanggilnya setelah memanggil list

lst = ['omega', 'alpha', 'pi', 'gamma']
print('list original',lst)
lst.sort()
print('list setelah dipanggil methodnya',lst)