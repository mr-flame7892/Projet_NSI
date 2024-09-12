import random

def rarityPicker():
    chance = random.randint(1, 100)
    if 35 <= chance <= 100:
        return "commun"
    elif 10 <= chance < 35:
        return "rare"
    elif 5 < chance < 10:
        return "épique"
    elif 1 < chance < 5:
        return "légendaire"
    elif chance == 1:
        return "mythique"

class chests:
    def __init__(self):
        self.length = 1000000000
        self.currentRarity = rarityPicker()
    def openChest(self):
        if self.length == 0:
            return "Vous n'avez pas de coffre !"
        self.length = self.length - 1
        print(f"Vous avez obtenu un item {self.currentRarity} !\nIl vous reste {self.length} coffre(s) !")
        self.currentRarity = rarityPicker()
        return
        

        
chest = chests()
