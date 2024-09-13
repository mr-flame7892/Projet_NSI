import random

class character:
    def __init__(self):
        self.startPV = 100
        self.startDMG = 5
        self.startDef = 5
        self.startSpeed = 30
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique de Cuire", "pv": 10/100, "def": 25/100}
        self.boots = { "name": "Bottes de cuir", "speed": 15/100 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 5/100 }
        self.exp = 0
        self.limitExp = 1
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.currentPV = self.startPV + self.startPV * self.armor["pv"]
        self.currentDef = self.startDef + self.startDef * self.armor["def"]
        self.currentSpeed = self.startSpeed + self.startSpeed * self.boots["speed"]
        self.currentDMG = self.startDMG + self.startDMG * self.weapon["dmg"]
    def getStats(self):
        print(f"Votre personnage à :\n\n- {self.currentPV} PV ({self.startPV} de base)\n- {self.currentDef} DEF ({self.startDef} de base)\n- {self.currentSpeed} SPEED ({self.startSpeed} de base)\n- {self.currentDMG} DMG ({self.startDMG} de base)")
        return
    def seeInventory(self):
        print(f"Votre personnage à :\n\n- Armure : {self.armor['name']}\n- Bottes : {self.boots['name']}\n- Arme : {self.weapon['name']}")
        return

character = character()


class monstres:
    def __init__(self):
        self.pv = 95
        self.attack = 4
        self.defence = 4
        self.boss = False

        chanceBoss = random.randint(1,100)
        
        if chanceBoss <= 20:
            self.boss = True

monstre = monstres()

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
