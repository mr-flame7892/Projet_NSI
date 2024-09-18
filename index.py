import random
import time

game = True

class character:
    def __init__(self):
        self.startPV = 100
        self.startDMG = 5
        self.startDef = 5
        self.startSpeed = 30
        self.startMana = 100
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "def": 10/100}
        self.boots = { "name": "Bottes en Cuir", "speed": 10/100 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 5/100 }
        self.exp = 0
        self.limitExp = 1
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.currentPV = self.startPV
        self.currentDef = round(self.startDef + self.startDef * self.armor["def"], 0)
        self.currentSpeed = round(self.startSpeed + self.startSpeed * self.boots["speed"], 0)
        self.currentDMG = round(self.startDMG + self.startDMG * self.weapon["dmg"], 0)
        
    def getStats(self):
        print(f"Votre personnage à :\n\n- {self.currentPV} PV ({self.startPV} de base)\n- {self.currentDef} DEF ({self.startDef} de base)\n- {self.currentSpeed} SPEED ({self.startSpeed} de base)\n- {self.currentDMG} DMG ({self.startDMG} de base)\n- {self.startMana} de mana (100 de base)")
        return
    
    def getInventory(self):
        print(f"Votre personnage à :\n\n- Armure : {self.armor['name']}\n- Bottes : {self.boots['name']}\n- Arme : {self.weapon['name']}")
        return
    
    def calculateStats(self):
        self.currentPV = self.startPV
        self.currentDef = round(self.startDef + self.startDef * self.armor["def"], 0)
        self.currentSpeed = round(self.startSpeed + self.startSpeed * self.boots["speed"], 0)
        self.currentDMG = round(self.startDMG + self.startDMG * self.weapon["dmg"], 0)
        return
    
    def resetCharacter(self):
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "def": 10/100}
        self.boots = { "name": "Bottes en Cuir", "speed": 10/100 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 5/100 }
        self.exp = 0
        self.limitExp = 1
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.calculateStats()
            

character = character()

listeMonstre=["Zombie","Squellette","Brigand","Araignée","la daronne d'enzo","Loup-Garou","sirene maléfique"]

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
        self.type=listeMonstre[random.randint(0,len(listeMonstre)-1)]
        self.pv = 95
        self.attack = 4
        self.defence = 4
        self.speed = 25
        self.currentPV = 95
        self.currentDef = 4
        self.currentSpeed = 25
        self.currentDMG = 4
        self.boss = False
        chanceBoss = random.randint(1,100)
        
        if (chanceBoss <= 20) and (character.room > 1):
            self.boss = True
        
    def getStats(self):
        print(f"Le monstre à :\n\n- {self.currentPV} PV ({self.pv} de base)\n- {self.currentDef} DEF ({self.defence} de base)\n- {self.currentSpeed} SPEED ({self.speed} de base)\n- {self.currentDMG} DMG ({self.attack} de base)")
        return

monstre = monstres()

"""def rarityPicker():
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
        
chest = chestsSystem()"""


class tour():
    def __init__(self):
        self.length = 0
        self.TypeTurn = None
        
rounds = tour()
        
def askPlayer():
    question = input("\n--------------------------------\n\nQuelle action voulez-vous réaliser ? (inventory/attaque/potion/monstre/stats) : ")
    
    if question == "inventory":
        print("\n--------------------------------\n")
        character.getInventory()
        return askPlayer()
    elif question == "attaque":
        return characterAttacks()
    elif question == "monstre":
        print("\n--------------------------------\n")
        monstre.getStats()
        return askPlayer()
    elif question == "stats":
        print("\n--------------------------------\n")
        character.getStats()
        return askPlayer()
    elif question == "potion":
        whichPotion = input("\n--------------------------------\n\nQuelle potion voulez-vous utiliser ? (vie/mana)\nPour retourner en arrière, utiliser return : ")
        if whichPotion == "vie":
            if character.currentPV == character.startPV:
                print("\n--------------------------------\n\nVotre vie est déjà pleine !")
                return askPlayer()
            character.items["PotionSoin"] = character.items["PotionSoin"] - 1
            character.currentPV = character.startPV
            print(f"\n--------------------------------\n\nVous avez récupéré tous vos PV !")
            return askPlayer()
        elif whichPotion == "mana":
            if character.startMana == 100:
                print("\n--------------------------------\n\nVotre mana est déjà rempli !")
                return askPlayer()
            character.items["PotionMana"] = character.items["PotionMana"] - 1
            gainedMana = 100 - character.startMana
            character.startMana = character.startMana + gainedMana
            print(f"\n--------------------------------\n\nVous avez récupéré tous votre mana !")
            return askPlayer()
    else:
        return askPlayer()
        
DMG = None
randomDMG = None

def characterAttacks():
    rounds.TypeTurn = "👤"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(1, 10)
    DMG = round((randomDMG * character.currentDMG) - ((randomDMG * character.currentDMG) * monstre.currentDef/100), 0)
    monstre.currentPV = round(monstre.currentPV - DMG, 0)
    if monstre.currentPV <= 0:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\n{monstre.type} s'est pris {DMG} DMG\nIl se désintégre sous vous yeux !")
        print(f"\n--------------------------------\n\nVous avez triomphé du mal, cependant il vous reste du chemin à parcourir...\n")
        reAsk()
    else:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\n{monstre.type}s'est pris {DMG} DMG\nIl lui reste {monstre.currentPV} PV !")
        time.sleep(2)
        monstreAttacks()


def monstreAttacks():
    rounds.TypeTurn = "💀"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(1, 10)
    DMG = round((randomDMG * monstre.currentDMG) - ((randomDMG * monstre.currentDMG) * character.currentDef/100), 0)
    character.currentPV = round(character.currentPV - DMG, 0)
    if character.currentPV <= 0:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nVous vous êtes pris {DMG} DMG\nIl vous n'êtes plus en état de vous battre !")
        print(f"--------------------------------\n\nLe mal a eu raison de vous...\nIl ne lui restait plus que {monstre.currentPV} PV\n")
        reAskGameOver()
    else:
        print(f"\n--------------------------------\n\n{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\nVous vous êtes pris {DMG} DMG\nIl vous reste {character.currentPV} PV !")
        askPlayer()


def reAskGameOver():
    restart = input("--------------------------------\n\nSouhaitez-vous recommencer ? (y/n) : ")
    if restart == "y":
        return launchGame()
    elif restart == "n":
        game = False
        exit()
        return
    else:
        reAskGameOver()
        
def reAsk():
    restart = input("--------------------------------\n\nSouhaitez-vous continuer ? (y/n) : ")
    if restart == "y":
        character.room = character.room + 1
        return launchRoom()
    elif restart == "n":
        game = False
        exit()
        return
    else:
        reAsk()
        

def launchRoom():
    print(f"Un/e {monstre.type} apparaît ")
    rounds.length = 0
    if character.room != 1:
        monstre.resetMonstre()
    if monstre.boss == True:
            i = 0
            while i <= 1:
                stat = random.randint(0, 3)
                if stat == 0:
                    monstre.currentPV = round((monstre.currentPV * 0.5) + monstre.currentPV, 0)
                elif stat == 1:
                    monstre.currentDMG = round((monstre.currentDMG * 0.5) + monstre.currentDMG, 0)
                elif stat == 2:
                    monstre.currentDef = round((monstre.currentDef * 0.5) + monstre.currentDef, 0)
                else:
                    monstre.currentSpeed = round((monstre.currentSpeed * 0.5) + monstre.currentSpeed, 0)
                i = i + 1
            print(f"--------------------------------\n\n⚠️ Un boss est aparu ! ⚠️\n\n{monstre.getStats()}\n")
    while monstre.currentPV >= 0 and character.currentPV >= 0:
        if monstre.currentSpeed < character.currentSpeed:
            askPlayer()
        else:
            monstreAttacks()

def launchGame():
    rounds.length = 0
    monstre.resetMonstre()
    character.resetCharacter()
    print("-----------------------\n \nVous vous réveillez sans aucun souvenir de la veille dans un recoin sombre d'une pièce froide et lugubre. \nUne grande porte en bois face a vous, vous l'ouvrez et......... ")
    while game == True:
        launchRoom()
                  
def askTuto():
    tuto = input("tuto ? (y/n) : ")

    if tuto == "y":
        print("Cher joueur, vous aller découvrir un jeux codé grâce au connaissance acquise en spé N.S.I :\n-----------------------\nLe jeux se joue avec la console de Thonny et est uniquement textuel suivez les instructions et profiter du jeu\n----------------------- ")
        input("Appuyez sur entrée quand vous êtes prêt !")
        launchGame()
    elif tuto == "n":
        launchGame()
    else:
        askTuto()

askTuto()
