# 6.1.4.1 OOP: Methods -6.1.4.2 OOP: Methods


# There is one fundamental requirement - a method is obliged to have at least one parameter(there are no such thing as parameterless methods - a method may be invoked without an argument, but not declared without parameters).
# self biasa digunakan untuk parameter, beberapa kondisi akan eror jika parameter pertama != self

class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()


class Classy2:
    def method(self, par):
        print("method:", par)


obj = Classy2()
obj.method(1)
obj.method(2)
obj.method(3)

class Classy3:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy3()
obj.var = 3
obj.method()

class Classy4:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy4()
obj.method()