# 3.1.2.15 LAB: Collatz's hypothesis

c0 = int(input("Enter the number : "))

while c0 <= 0 :
    print("must positive and greater than 0")
    c0 = int(input("Enter the number : "))

step = 0

while c0 != 1:
    step +=1
    print(c0)
    if c0 % 2 == 0:
        c0 //= 2
    else :
        c0 = 3 * c0 + 1
print(1)
print("step = ",step)