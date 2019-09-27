# 4.1.3.4 Returning a result from a function

def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
    
print(sumOfList([5, 4, 3]))