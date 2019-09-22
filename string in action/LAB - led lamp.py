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