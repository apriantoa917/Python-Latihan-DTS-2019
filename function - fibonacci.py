# 4.1.5.7 Creating functions | Fibonacci numbers

def Fibonacci(lim):
    counter = 1
    f1 = 1
    f2 = 1
    while(counter <= lim):
        if(counter <= 2):
            f3 = 1
        else:
            f3 = f1 + f2
            f1,f2 = f2,f3
        counter += 1
    return print("fib",lim,":",f3)
        

for i in range(1,11):
    Fibonacci(i)