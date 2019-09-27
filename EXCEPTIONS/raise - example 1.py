# def badFun(n):
#     raise ZeroDivisionError

# try:
#     badFun(0)
# except ArithmeticError:
#     print("What happened? An error?")

# print("THE END.")

# 5.1.5.6 The anatomy of exceptions | raise


def badFun(n):
    try:
        return n / 0
    except:
        if n == 0:
            print("I did it again!")
            # raise menyebabkan kode masuk ke except terdekat yang memenuhi kondisi.
            raise
            # kode masuk kedalam except ini karena pembagian angka dengan 0 (ZeroDivisionError) dan akan menjalankan except terdekat
            # (ArithmeticError) karena except itu general class dari ZeroDivisionError
        else:
            print("I didn't it again!")
            print('------------------')


try:
    badFun(4)
    badFun(0)
except ArithmeticError:
    print("I see!")
    print('------------------')


print("THE END.")

try:
    try:
        a = 1/0
        print("saya masih try")
    except:
        print("saya masuk except 1")
        print("----- raise -----")
        raise   # raise hanya dapat dipanggil di kondisi except untuk mengeluarkan except yang lain
except :
    print("saya masuk except 2")