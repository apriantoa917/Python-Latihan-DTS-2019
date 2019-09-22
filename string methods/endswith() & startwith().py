# 5.1.9.3 String methods

# endswith() = ends with = mengecek apakah akhiran dari suatu kata mengandung kata yang dimaksud dan mengembalikan nilai T/F

kata = 'Hello'

print(kata.endswith('a'))
print(kata.endswith('o'))

def check(kata,cari):
    if kata.endswith(cari):
        print(kata,'berakhiran dengan',cari)
    else:
        print(kata,'tidak berakhiran dengan',cari)

check(kata,'elo')
check(kata,'ello')
check(kata,'o')
check(kata,'e')
check('aprianto','a')
check('aprianto','o')

# startwith = mengecek apakah suatu kata diawali dengan karakter tertentu, megembalikan nilai T/F

print("omega".startswith("meg"))
print("omega".startswith("om"))
