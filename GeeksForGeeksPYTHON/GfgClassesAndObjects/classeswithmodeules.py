import methods

p = methods.Player("Shuv", 22, 85, 78, 71, 80)

st = int(input("Add Strength to the Player:"))
p.addStrength(st)

sm = int(input("Add Stamina to the Player:"))
p.addStamina(sm)

ag = int(input("Add Agility to the Player:"))
p.addAgility(ag)

inte = int(input("Add Intelligence to the Player:"))
p.addIntelligence(inte)
