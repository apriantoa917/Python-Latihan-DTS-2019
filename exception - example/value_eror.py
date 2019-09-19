# 5.1.4.1 Errors - the programmer

import math

x = float(input("Enter x: ")) 
# input string here, res : ValueError: could not convert string to float: '...'
# input negative here, res : ValueError: math domain error
y = math.sqrt(x)

print("The square root of", x, "equals to", y)