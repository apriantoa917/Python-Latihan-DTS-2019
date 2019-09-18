# print('I like to be a module.')
# print(__name__)
# if __name__ == "__main__":
#     print("saya dijalankan di :",__name__)
# else:
#     print("saya menjalankan :",__name__)

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)