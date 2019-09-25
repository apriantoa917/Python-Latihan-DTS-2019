# 6.1.2.10 A short journey from procedural to object approach

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
        for i in range(1,6):
            self.push(i)

        for i in range(1,6):
            a = self.pop()
            self.__sum += a
            print(a)
        
        print('sum :',self.__sum)
        

AddingStack()

