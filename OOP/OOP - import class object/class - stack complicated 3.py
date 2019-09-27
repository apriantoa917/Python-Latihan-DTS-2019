# 6.1.2.9 A short journey from procedural to object approach

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

littleStack = Stack()
anotherStack = Stack()
funnyStack = Stack()

littleStack.push(1)
anotherStack.push(littleStack.pop() + 1)
funnyStack.push(anotherStack.pop() - 2)

print(funnyStack.pop())