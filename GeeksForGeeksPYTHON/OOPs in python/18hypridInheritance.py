class a:
    pass
class b:
    pass
class c:
    pass
class x(a,b,c):
    pass
class y(b,c):
    pass
class p(x,y):
    pass

print(p.mro())