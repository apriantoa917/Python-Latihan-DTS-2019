#  5.1.6.4 Reading ints safely

def readint(prompt, min, max):
    cek = False
    while not cek:
        try:
            val = int(input(prompt))
            cek = True
        except:
            print('Wrong input')
    if cek :
        if val >= -10 and val <= 10:
            return val
        else:
            print('over the limit')
        

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)