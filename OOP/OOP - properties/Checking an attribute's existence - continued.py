# 6.1.3.8 OOP: Properties

class ExampleClassTrial:
    attr = 1

print(hasattr(ExampleClassTrial, 'attr'))
print(hasattr(ExampleClassTrial, 'prop'))

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

print(hasattr(exampleObject, 'b'))
print(hasattr(exampleObject, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))