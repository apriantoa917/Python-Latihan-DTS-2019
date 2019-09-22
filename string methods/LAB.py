# 5.1.9.18 Your own split

def mysplit(strng):
    lst = []
    lst = strng.split()
    return lst

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))