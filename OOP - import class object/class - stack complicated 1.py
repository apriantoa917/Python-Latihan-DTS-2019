# 6.1.2.7 A short journey from procedural to object approach

class Stack:
    def __init__(self):
        self.__stackList = []   # private list, hanya bisa diakses di kelas Stack

    def push(self, val):
        self.__stackList.append(val)

    def pop(self,i):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        text = 'keluar ke-'+str(i)+' : '+val
        return text


stackObject = Stack()

for i in range(1,6):
    text = 'masuk ke-'+str(i)
    stackObject.push(text)

for i in range(1,6):
    print(stackObject.pop(i))
