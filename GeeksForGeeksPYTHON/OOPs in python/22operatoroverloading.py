class a:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):#operator overloading
        real= self.x+other.x
        img=self.y+other.y
        return f"{real} + {img}i"
    def __sub__(self,other):
        real=self.x-other.x
        img=self.y-other.y
        return f"{real}+{img}i"

oa=a(9,9)
ob=a(7,8)
print(oa+ob)
print(oa-ob)