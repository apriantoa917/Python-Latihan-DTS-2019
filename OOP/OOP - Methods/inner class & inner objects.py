# 6.1.4.5 OOP: Methods

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        self.__hidden()

    def __hidden(self):
        print('hidden')

obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)

print()
print(obj.method())

