# methods.py
class Player:
    def __init__(self, name, age, strength, stamina, agility, intelligence):
        self.name = name
        self.age = age
        self.strength = strength
        self.stamina = stamina
        self.agility = agility
        self.intelligence = intelligence
        self.print_details()
        
    def print_details(self):
        print("_______Details of the Player_______")
        print(self.name, self.age, self.strength, self.stamina, self.agility, self.intelligence)
        
    def addStrength(self, power):
        self.strength += power
        print("Current Strength:", self.strength)
        
    def addStamina(self, ste):
        self.stamina += ste
        print("Current Stamina:", self.stamina)
        
    def addAgility(self, agi):
        self.agility += agi
        print("Current Agility:", self.agility)
        
    def addIntelligence(self, inte):
        self.intelligence += inte
        print("Current Intelligence:", self.intelligence)
