# 3.1.2.10 LAB: The continue statement - the Ugly Vowel Eater

userWord = input("Enter the word : ")
userWord = userWord.upper()

for letter in userWord : 
    if (letter == "A" or letter == "I" or letter == "U" or letter == "E" or letter == "O"):
        continue
    print(letter)