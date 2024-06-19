def iseven(value):
    return value%2==0
        
l=[3,4,5,6,7,8,9]
print(list(filter(iseven,l)))