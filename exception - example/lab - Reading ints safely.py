#  5.1.6.4 Reading ints safely

def readint(prompt, min, max):
    # bertanya inputan :
    try:
        val = int(input("Enter a number from -10 to 10:"))
    except :
        print('Error: wrong input')
    if val >= -10 and val <= 10:
        pass
    else:
        print('Error: the value is not within permitted range (',min,'..',max,')')
    return val
        

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)