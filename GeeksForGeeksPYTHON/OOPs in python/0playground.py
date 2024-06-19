class Animal:
    speak="Can Speak"
    eat="Can Eat"
    def properties(self):
        print("This is a animal class")
        print(self.speak)
        print(self.eat)
class Cat(Animal):
    def catproperties(self):
        print("This is a cat class")
        print(self.speak)
        print(self.eat)
class Dog(Animal):
    def dogproperties(self):
        print("This is a dog class")
        print(self.speak)
        print(self.eat)
class GoldenRetriver(Dog):
    color="Golden"
    type="Playfull"
    def goldenretiverproperties(self):
        print("This is a golden retiver class")
        print("It has ",self.color,"furr and it is",self.type,"type dog")
        print(self.speak)
        print(self.eat)

c=Cat()
c.catproperties()
print()
d=Dog()
d.dogproperties()
print()
g=GoldenRetriver()
g.goldenretiverproperties()