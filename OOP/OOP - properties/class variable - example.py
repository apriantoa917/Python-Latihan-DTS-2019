# 6.1.3.3 OOP: Properties

class ExampleClass:
    counter = 0
    print('counter setelah inisialisasi: ',counter)
    def __init__(self, val = 1):
        self.__first = val
        print('counter masuk constructor: ',ExampleClass.counter)
        ExampleClass.counter += 1
        print('counter penambahan : ',ExampleClass.counter)

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)
exampleObject4 = ExampleClass(45)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)
