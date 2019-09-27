# 3.1.7.1 Lists in advanced applications

# list squares = square value of 10 items start from 0

squares = [x ** 2 for x in range(10)]

print("squares : ",squares)

# list odds = odd values of list square

odds = [ x for x in squares if x % 2 != 0]

print("odds : ",odds)

# list even = even values of list square

even = [ x for x in squares if x % 2 == 0]

print("even : ",even)

# -----------------------------------------------------

# list twos = values of 2 powered by numbers in range (10)

twos = [ 2 ** x for x in range(10)]

print(" 2 ^ 10 : ",twos)