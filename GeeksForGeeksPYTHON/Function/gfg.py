# gfg.py

def greet(name):
    return "Hello " + name

def ngreet():
    return "Hello"

def add(a=5, b=6):
    return a + b

def operation(a, b):
    return a + b, a - b, a * b

lst = [3, 4, 5, 6, 7, 8, 9]

def sqlist(l):
    return [i * i for i in l]

def cubelist(l):
    return [i * i * i for i in l]

def addi(lst):
    l = sqlist(lst)
    ll = cubelist(lst)
    return [l[i] + ll[i] for i in range(len(lst))]

if __name__ == "__main__":
    print(greet("Shuv"))
    print([ngreet() for i in range(10)])
    print(add(5, 7))
    print(operation(5, 6))
    print(type(operation(5, 6)))
    print(sqlist(lst))
    print(cubelist(lst))
    print(addi(lst))
