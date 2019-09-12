# 4.1.5.4 Creating functions | testing triangles

# pytagoras

# c^2 = a^2 + b^2 -> a < c & b < c
# a^2 = c^2 - b^2 -> a < c & a > b
# b^2 = c^2 - a^2 -> b < c & b < a

# check if side can applied pythagoras
def isItATriangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def isItRightTriangle(a, b, c):
    if isItATriangle(a,b,c):
        if c > a and c > b:
            return c ** 2 == a ** 2 + b ** 2
        if a > b and a > c:
            return a ** 2 == b ** 2 + c ** 2
    else:
        return False

print(isItRightTriangle(5, 3, 4))
print(isItRightTriangle(1, 3, 4))