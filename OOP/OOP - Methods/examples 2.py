# 6.1.4.3 OOP: Methods

class Classy:
    def __init__(self, value):
        self.var = value

obj1 = Classy("object")

print(obj1.var)

# constructor : 
#tidak dapat mengembalikan nilai, karena ini dirancang untuk mengembalikan objek yang baru dibuat dan tidak ada yang lain;
# # tidak dapat dipanggil secara langsung baik dari objek atau dari dalam kelas (Anda dapat memanggil konstruktor dari superclasses objek mana pun,

class Classy2:
    def __init__(self, value = None):
        self.var = value

obj1 = Classy2("Ini sebuah value")
obj2 = Classy2()

print(obj1.var)
print(obj2.var)

class Classy3:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

obj = Classy3()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy3__hidden()  # untuk mengakses method private 