class a:
    def sum(self,a,b):
        print(a+b)
class b(a):
    def sum(self,a,b,c):
        print(a+b+c)

oa=a()
oa.sum(5,6)
ob=b()
ob.sum(5,6,7)