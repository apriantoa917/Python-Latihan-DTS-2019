# 6.1.2.4 A short journey from procedural to object approach

class Stack:    # defining the Stack class
    def __init__(self):    # defining the constructor function, constructor diawali dengan __init__()
        print("Hi!")

stackObject = Stack()    # instantiating the object

# 6.1.2.5 A short journey from procedural to object approach

class Stack1:
    def __init__(self):
        self.stackList = ['1','2']

stackObject1 = Stack1()
print(len(stackObject1.stackList))