# 4.1.5.3 Creating functions | three-parameter functions

# default function

def isItATriangle1(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(isItATriangle1(1, 1, 1))
print(isItATriangle1(1, 1, 3))

# more compact

def isItATriangle2(a, b, c):
    if a + b <= c or b + c <= a or \
    c + a <= b:
        return False
    return True

print(isItATriangle2(1, 1, 1))
print(isItATriangle2(1, 1, 3))

# more compact

def isItATriangle3(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(isItATriangle3(1, 1, 1))
print(isItATriangle3(1, 1, 3))