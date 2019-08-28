#3.1.1.12 LAB: Essentials of the if-else statement

income = float(input("Enter the annual income: "))

if income <= 85528 :
    tax = ((18/100) * income) - 556.2
elif income >= 85528 :
    tax = 14839.2 + ((32/100) * (income - 85528))

if tax <= 0 :
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")