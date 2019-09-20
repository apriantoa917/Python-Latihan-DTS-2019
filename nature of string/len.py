# 5.1.8.1 The nature of strings in Python

# Example 1

word = 'by'
print(len(word))


# Example 2

empty = ''
print(len(empty))


# Example 3

i_am = 'I\'m'
print(len(i_am))



multiLine = '''Line #1
Line #2''' # result = 15 (semua karakter (termasuk spasi) dengan penambahan enter \n)

print(len(multiLine))

multiLine = """Line #1
Line #2"""  # hasil sama antara singe quote & double quote

print(len(multiLine))