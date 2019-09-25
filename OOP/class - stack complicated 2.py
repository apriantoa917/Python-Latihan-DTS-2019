# 6.1.2.8 A short journey from procedural to object approach

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


stackObject1 = Stack()
stackObject2 = Stack()

stackObject1.push(3)
stackObject2.push(stackObject1.pop())

print(stackObject2.pop())