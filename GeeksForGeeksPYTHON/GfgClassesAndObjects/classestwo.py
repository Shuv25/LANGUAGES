class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(self.name)
        print(self.age)

p1=Person("Shuv",22)
p1.details()