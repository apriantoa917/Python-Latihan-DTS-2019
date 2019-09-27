# 4.1.5.6 Creating functions | factorials

# 0! = 1 (yes! it's true)
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4
# :
# :
# n! = 1 * 2 ** 3 * 4 * ... * n-1 * n

def factorials(num):
    res = 1
    if(num < 0):
        return print(num,"! = minimal limit = 0")   
    for i in range(1,num+1):
        res = i * res
    print( num,"! = ",res)

for a in range(-5,11):
    factorials(a)