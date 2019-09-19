# 5.1.5.4 The anatomy of exceptions

def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        return("Arithmetic Problem!")
    

for i in range(5):
    print(i,'->',badFun(i))
