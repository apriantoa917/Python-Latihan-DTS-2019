# 5.1.10.4 String in action

integers = 12
string = '12'

# print(integers+string) eror karena tipe data tidak sama, int tidak bisa di operasikan dengan str

IntToString = str(integers)
StringToInt = int(string)

print('hasil int + int',integers+StringToInt)
print('hasil str + str',string+IntToString)

floats = 1.98
StringToFloat = float(string)
FloatToString= str(floats)
print('hasil float + float',floats+StringToFloat)
print('hasil str + str',string+FloatToString)