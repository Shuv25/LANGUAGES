class ReserveBank:
    rate=0.05
    def __init__(self):
        print("Reserve Bank Contsractor is called")

class StateBank(ReserveBank):
    def __init__(self,p,t):
        super().__init__()
        print("SI in State Bank of India is:")
        print((p*self.rate*t)/100)

class UCOBank(StateBank):
    def __init__(self,p,t):
        super().__init__(p,t)
        print("SI in UCO Bank is:")
        print((p*self.rate*t)/100)

u=UCOBank(6000,1/2)
