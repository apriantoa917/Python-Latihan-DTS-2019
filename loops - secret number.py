#3.1.2.3 LAB: Essentials of the while loop - Guess the secret number

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

user = int(input("enter the secret  number : "))

while secret_number != user :
    print("Ha ha! You're stuck in my loop!")
    user = int(input("enter the secret  number : "))
    
    
print("Well done, muggle! You are free now.")