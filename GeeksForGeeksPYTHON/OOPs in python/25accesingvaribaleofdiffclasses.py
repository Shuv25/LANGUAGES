class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(self.name)
        print(self.sal)

class changes:
    @staticmethod
    def incre(obj):
        obj.sal=obj.sal+500000
        obj.display()

e=employee("Shuv",70000000)
e.display()
c=changes()
c.incre(e)