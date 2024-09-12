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
    
class character:
    def __init__(self):
        self.pv = 100
        self.attack = 5
        self.defence = 5
        self.items = []
        self.exp = 0
        self.mana = 20
        self.limitExp = 1
        self.lvl = 1
        self.chests = 1

character = character()


class monstres:
    def __init__(self):
        self.pv = 95
        self.attack = 4
        self.defence = 4
       

class chestsSystem:
    def __init__(self):
        self.currentRarity = rarityPicker()
        self.item = "Bâton"
    def openChest(self):
        if character.chests == 0:
            return "Vous n'avez pas de coffre !"
        character.chests = character.chests - 1
        character.items.append(self.item)
        print(f"Vous avez obtenu un item {self.currentRarity} !\nIl vous reste {character.chests} coffre(s) !")
        self.currentRarity = rarityPicker()
        return
        
chest = chestsSystem()

chest.openChest()
