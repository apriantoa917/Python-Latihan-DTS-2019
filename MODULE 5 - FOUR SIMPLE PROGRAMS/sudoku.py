# 5.1.11.11 LAB: Sudoku

data = ['' for i in range(9)]

def inputData(i):
    temp = input('masukan data ke-'+str(i+1)+' : ')
    if not temp.isdigit() or len(temp) != 9:
        print('input harus berupa angka dan memiliki 9 digit')
        inputData(i)
    else:
        for j in range(3):
            counter = 0
            for angka in temp[j]:
                data[j].append(angka)
                counter+=1
        print(data)

for i in range(3):
    inputData(i) 