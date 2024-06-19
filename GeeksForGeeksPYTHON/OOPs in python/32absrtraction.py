from abc import ABC,abstractclassmethod
class atm:
    @abstractclassmethod
    def witdraw(self):
        pass
    @abstractclassmethod
    def deposit(self):
        pass
    @abstractclassmethod
    def show_balance(self):
        pass
    @abstractclassmethod
    def reciept(self):
        pass
    @abstractclassmethod
    def pin_change(self):
        pass

class customer(atm):
    def __init__(self,amount,neg,pos,pin):
        self.amount=amount
        self.neg=neg
        self.pos=pos
        self.pin=pin
    def witdraw(self):
        self.amount=self.amount-self.neg
        print("Witdraw amount is ",self.neg," remaining amont is ",self.amount)
    def deposit(self):
        self.amount=self.amount+self.pos
        print("Added amount is ",self.pos," remaining amont is ",self.amount)
    def show_balance(self):
        print("Your current bank balance is ",self.amount)
    def reciept(self):
        print("Witdraw amount is ",self.neg," remaining amont is ",self.amount)
        print("Added amount is ",self.pos," remaining amont is ",self.amount)
        print("Your current bank balance is ",self.amount)
        print("Your pin is ",self.pin)
    def pin_change(self,newpin):
        self.pin=newpin
        print("The new pin is ",self.pin)

c=customer(30000000,80000,90000,789)
c.witdraw()
c.deposit()
c.show_balance()
c.reciept()
c.pin_change(987)

