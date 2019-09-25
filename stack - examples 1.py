# 6.1.2.2 A short journey from procedural to object approach

stack = []

def push(val):
    stack.append(val)


def pop(i):
    val = stack[-1]
    del stack[-1]
    text = 'keluar ke-'+str(i)+' : '+val
    return text

for i in range(1,6):
    text = 'masuk ke-'+str(i)
    push(text)

for i in range(1,6):
    print(pop(i))