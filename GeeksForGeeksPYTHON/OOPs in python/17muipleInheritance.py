class Mother:
    car="Porche 911"
    def __init__(self):
        print("Mother Constractor is called")

class Father:
    bike="Kawasaki Ninza H2R"
    def __init__(self):
        print("Father Constractor is called")

class Son(Mother,Father):
    def __init__(self):
        super().__init__()
        Father.__init__(self)
        print("Son Constractor is called")
        print(self.car," ",self.bike)

s=Son()