import random

game = True

class character:
    def __init__(self):
        self.startPV = 100
        self.startDMG = 5
        self.startDef = 5
        self.startSpeed = 30
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "pv": 10/100, "def": 10/100}
        self.boots = { "name": "Bottes en Cuir", "speed": 10/100 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 15/100 }
        self.exp = 0
        self.limitExp = 1
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.currentPV = round(self.startPV + self.startPV * self.armor["pv"], 0)
        self.currentDef = round(self.startDef + self.startDef * self.armor["def"], 0)
        self.currentSpeed = round(self.startSpeed + self.startSpeed * self.boots["speed"], 0)
        self.currentDMG = round(self.startDMG + self.startDMG * self.weapon["dmg"], 0)
        
    def getStats(self):
        print(f"Votre personnage à :\n\n- {self.currentPV} PV ({self.startPV} de base)\n- {self.currentDef} DEF ({self.startDef} de base)\n- {self.currentSpeed} SPEED ({self.startSpeed} de base)\n- {self.currentDMG} DMG ({self.startDMG} de base)")
        return
    
    def seeInventory(self):
        print(f"Votre personnage à :\n\n- Armure : {self.armor['name']}\n- Bottes : {self.boots['name']}\n- Arme : {self.weapon['name']}")
        return
    
    def calculateStats(self):
        self.currentPV = round(self.startPV + self.startPV * self.armor["pv"], 0)
        self.currentDef = round(self.startDef + self.startDef * self.armor["def"], 0)
        self.currentSpeed = round(self.startSpeed + self.startSpeed * self.boots["speed"], 0)
        self.currentDMG = round(self.startDMG + self.startDMG * self.weapon["dmg"], 0)
        return
    
    def resetCharacter(self):
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "pv": 5/100, "def": 10/100}
        self.boots = { "name": "Bottes en Cuir", "speed": 10/100 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 15/100 }
        self.exp = 0
        self.limitExp = 1
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.calculateStats()
            

character = character()

class monstres:
    def __init__(self):
        self.pv = 95
        self.attack = 4
        self.defence = 4
        self.speed = 25
        self.boss = False
        self.currentPV = self.pv
        self.currentDef = self.defence
        self.currentSpeed = self.speed
        self.currentDMG = self.attack

        chanceBoss = random.randint(1,100)
        
        if (chanceBoss <= 20) and (character.room > 1):
            self.boss = True
            
    def resetMonstre(self):
        self.pv = 95
        self.attack = 4
        self.defence = 4
        self.speed = 25
        self.currentPV = 95
        self.currentDef = 4
        self.currentSpeed = 25
        self.currentDMG = 4
        
    def getStats(self):
        return f"Le monstre à :\n\n- {self.currentPV} PV ({self.pv} de base)\n- {self.currentDef} DEF ({self.defence} de base)\n- {self.currentSpeed} SPEED ({self.speed} de base)\n- {self.currentDMG} DMG ({self.attack} de base)"

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

DMG = None
randomDMG = None

class tour():
    def __init__(self):
        self.length = 0
        self.TypeTurn = None
        
rounds = tour()

def characterAttacks():
    rounds.TypeTurn = "👤"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(1, 10)
    DMG = round((randomDMG * character.currentDMG) - ((randomDMG * character.currentDMG) * monstre.currentDef/100), 0)
    monstre.currentPV = round(monstre.currentPV - DMG, 0)
    if monstre.currentPV <= 0:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nLe monstre s'est pris {DMG} DMG\nIl se désintégre sous vous yeux !")
        print(f"--------------------------------\n\nVous avez triomphé du mal, cependant il vous reste du chemin à parcourir...\n")
        restart = input("--------------------------------\n\nSouhaitez-vous recommencer ? (y/n)")
        if restart == "y":
            character.room = character.room + 1
            monstre.resetMonstre()
            return launchRoom()
        elif restart == "n":
            game = False
            exit()
            return
    else:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nLe monstre s'est pris {DMG} DMG\nIl lui reste {monstre.currentPV} PV !")
        input("\n--------------------------------\n\nAppuyez sur Entrée pour continuer le combat")
        monstreAttacks()
            
def monstreAttacks():
    rounds.TypeTurn = "💀"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(1, 5)
    DMG = round((randomDMG * monstre.currentDMG) - ((randomDMG * monstre.currentDMG) * character.currentDef/100), 0)
    character.currentPV = round(character.currentPV - DMG, 0)
    if character.currentPV <= 0:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nVous vous êtes pris {DMG} DMG\nIl vous n'êtes plus en état de vous battre !")
        print(f"--------------------------------\n\nLe mal a eu raison de vous...\nIl ne lui restait plus que {monstre.pv} PV\n")
        restart = input("--------------------------------\n\nSouhaitez-vous recommencer ? (y/n)")
        if restart == "y":
            return launchGame()
        elif restart == "n":
            game = False
            exit()
            return
    else:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nVous vous êtes pris {DMG} DMG\nIl vous reste {character.currentPV} PV !")
        input("\n--------------------------------\n\nAppuyez sur Entrée pour continuer le combat")
        characterAttacks()

def launchRoom():
    rounds.length = 0
    if monstre.boss == True:
            i = 0
            while i <= 1:
                stat = random.randint(0, 4)
                if stat == 0:
                    monstre.currentPV = round((monstre.currentPV * 0.5) + monstre.currentPV, 0)
                elif stat == 1:
                    monstre.currentDMG = round((monstre.currentDMG * 0.5) + monstre.currentDMG, 0)
                elif stat == 2:
                    monstre.currentDef = round((monstre.currentDef * 0.5) + monstre.currentDef, 0)
                else:
                    monstre.currentSpeed = round((monstre.currentSpeed * 0.5) + monstre.currentSpeed, 0)
                i = i + 1
            print(f"--------------------------------\n\n⚠️ Un boss est aparu ! ⚠\n\n{monstre.getStats()}\n")
    while monstre.currentPV >= 0 and character.currentPV >= 0:
        if monstre.currentSpeed < character.currentSpeed:
            characterAttacks()
        else:
            monstreAttacks()

def launchGame():
    rounds.length = 0
    monstre.resetMonstre()
    character.resetCharacter()
    while game == True:
        launchRoom()
                  
def askTuto():
    tuto = input("tuto ? (y/n)")

    if tuto == "y":
        print("Chère joueur, vous aller découvrir un jeux codé grâce au connaissance acquise en spé N.S.I :\n-----------------------\nLe jeux se joue avec la console de Thonny et est uniquement textuel suivez les instructions et profiter du jeu\n----------------------- ")
        input("Appuyez sur entrée quand vous êtes prêt !")
        launchGame()
    elif tuto == "n":
        launchGame()
    else:
        askTuto()

askTuto()
