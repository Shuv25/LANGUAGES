from abc import ABC,abstractclassmethod

class car(ABC):
    @abstractclassmethod
    def mileage(self):
        pass
    def colour(self):
        print("White")

class suzuki(car):
    def mileage(self):
        print("30km/L")

class tata(car):
    def mileage(self):
        print("35km/L")

class jeep(car):
    def mileage(self):
        print("40km/L")

s=suzuki()
s.mileage()
s.colour()
t=tata()
t.mileage()
t.colour()
j=jeep()
j.mileage()
j.colour()
