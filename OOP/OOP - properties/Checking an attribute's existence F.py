# 6.1.3.6 OOP: Properties

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)

print(exampleObject.a)
print(exampleObject.b)

#EROR RESULT