# 5.1.9.8 String methods

# join()= menggabungkan beberapa elemen string menjadi 1 dengan separator tertentu
# elemen string berupa list

# Demonstrating the join() method
print(",".join(["omicron", "pi", "rho"]))

lst = ['kata pertama','kata kedua','kata ketiga','kata keempat']
print(', lalu ini '.join(lst))

# split() = menggabungkan sebuah kata / kalimat menjadi setiap elemen list

kata = 'ini adalah sebuah kalimat yang tidak utuh, biasa dibilang frasa\nini adalah baris kedua'

lst = kata.split()

print(kata)
print(lst)