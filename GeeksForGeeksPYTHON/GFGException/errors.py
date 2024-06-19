a=int(input("First No:"))
b=int(input("Second No:"))
l=[3,4,5,6]
try:
    c=a/b
    x=l[5]
except ZeroDivisionError as z:
    print("Error->",z)
except IndexError as i:
    print("Error->",i)
else:
    print(c)
    print(x)
finally:
    print("This line will print doesnt matter if program has any error or not")