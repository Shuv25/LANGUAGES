class Car:
    def __init__(self,wheel):
        self.wheel=wheel

class Porsche(Car):
    def __init__(self,wheel,color):
        super().__init__(wheel)
        self.color=color
    def details(self):
        print(self.wheel,self.color)

c=Porsche(4,"Red")
c.details()