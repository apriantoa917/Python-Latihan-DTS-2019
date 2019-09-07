# 4.1.3.5 Returning a result from a function

def strangeListFunction(n):
    strangeList = []
    
    # reverse list
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))