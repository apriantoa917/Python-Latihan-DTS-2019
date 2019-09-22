# 5.1.10.6 LAB: A LED Display

pola = [['*****','*   *','*   *','*   *','*****'], # index 0
        ['   * ','  ** ','   * ','   * ','  ***'], # index 1
        ['*****','    *','*****','*    ','*****'], # index 2
        ['*****','    *','*****','    *','*****'], # index 3
        ['*   *','*   *','*****','    *','    *'], # index 4
        ['*****','*    ','*****','    *','*****'], # index 5
        ['*****','*    ','*****','*   *','*****'], # index 6
        ['*****','    *','    *','    *','    *'], # index 7
        ['*****','*   *','*****','*   *','*****'], # index 8
        ['*****','*   *','*****','    *','*****']] # index 9

def inputan():
    try:
        angka = int(input('Masukan angka yang akan dicetak : '))
    except:
        print('Inputan yang anda masukan tidak valid, inputan harus berupa angka')
        inputan()
    dump = list(str(angka))
    lst = [int(a) for a  in dump]
    print(lst)
    for i in range(5):
        for j in lst:
            print(pola[j][i],end=' ')
        print()
inputan()

# sample solution edube------------------------------------------------

# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]

# def printNumber(num):
# 	global digits
# 	digs = str(num)
# 	lines = [ '' for l in range(5) ]
# 	for d in digs:
# 		segs = [ [' ',' ',' '] for l in range(5) ]
# 		ptrn = digits[ord(d) - ord('0')]
# 		if ptrn[0] == '1':
# 			segs[0][0] = segs[0][1] = segs[0][2] = '#'
# 		if ptrn[1] == '1':
# 			segs[0][2] = segs[1][2] = segs[2][2] = '#'
# 		if ptrn[2] == '1':
# 			segs[2][2] = segs[3][2] = segs[4][2] = '#'
# 		if ptrn[3] == '1':
# 			segs[4][0] = segs[4][1] = segs[4][2] = '#'
# 		if ptrn[4] == '1':
# 			segs[2][0] = segs[3][0] = segs[4][0] = '#'
# 		if ptrn[5] == '1':
# 			segs[0][0] = segs[1][0] = segs[2][0] = '#'
# 		if ptrn[6] == '1':
# 			segs[2][0] = segs[2][1] = segs[2][2] = '#'
# 		for l in range(5):
# 			lines[l] += ''.join(segs[l]) + ' '
# 	for l in lines:
# 		print(l)

# printNumber(int(input("Enter the number you wish to display: ")))