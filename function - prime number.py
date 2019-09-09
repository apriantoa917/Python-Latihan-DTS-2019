# 4.1.3.9 LAB: Prime numbers - how to find them


# full apri

prime_number=[]

def isPrime(bil):
    prima = True
    divisor = 2
    if(bil ==1):
        return False
    elif(bil == 2):
        prime_number.append(bil)
        return True
    else:
        while(prima and divisor < bil):
            if(bil % divisor == 0):
                prima = False
            else:
                if(divisor == bil-1):
                    prime_number.append(bil)
            divisor += 1
        if(prima):
            return True
        else:
            return False

for i in range(1,30):
    print(i," prima ? =",isPrime(i))

print(prime_number)


# versi edube
# def isPrime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if isPrime(i + 1):
#         print(i + 1, end=" ")
# print()