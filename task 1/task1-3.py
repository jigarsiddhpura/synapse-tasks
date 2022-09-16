
class Titandex:
    def __init__(self, nm, he, st, ws):
        self.name = nm
        self.height = he
        self.strength = st
        self.win_streak = ws
    
    def TitanvsScout(self, name_scout, strength_scout):

        if self.strength > strength_scout:
            self.win_streak += 1
            print(f"{self.name} wins over {name_scout}")
        elif self.strength < strength_scout:
            print(f"{name_scout} wins over {self.name}")
        else:
            print(f"Match is a Draw")

    def TitanvsTitan(self, titan2):

        if self.strength > titan2.strength:
            self.win_streak += 1
            print(f"{self.name} wins over {titan2.name}")
        elif self.strength < titan2.strength:
            print(f"{titan2.name} wins over {self.name}")
            titan2.win_streak += 1
        elif self.name == titan2.name:
            print(f"{titan2.name} cannot fight itself")
        else:
            print(f"Match is a Draw")


Founding_Titan = Titandex('Founding_Titan', 13, 350, 0)
Attack_Titan = Titandex('Attack_Titan', 15, 275, 0)
Armored_Titan = Titandex('Armored_Titan', 15, 250, 0)
Collosal_Titan = Titandex('Collosal_Titan', 60, 300, 0)

Founding_Titan.TitanvsScout("Levi",300)
Founding_Titan.TitanvsScout("Mikasa",275)
print(Founding_Titan.win_streak)

Armored_Titan.TitanvsScout("Levi",300)
Armored_Titan.TitanvsScout("Mikasa",275)
Armored_Titan.TitanvsScout("Connie",180)
print(Armored_Titan.win_streak)


    

