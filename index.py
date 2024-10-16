import random
import time

game = True

listItemsCommon = [{'name':'Baton', 'stat' : 5, 'prix' : 300, 'type' : 'dmg'}]
listItemsRare = [{'name':'Bottes Symbiotiques', 'stat' : 10, 'prix': 700, 'type' : 'speed'}]
listItemsEpic = [{'name':'Coeuracier', 'stat' : 10, 'prix' : 1000, 'type': 'def'}]
listItemsLegendary = []
listItemsMythic = []

listRarities = [listItemsCommon, listItemsRare, listItemsEpic, listItemsLegendary, listItemsMythic]

class character:
    def __init__(self):
        self.startPV = 100
        self.startDMG = 5
        self.startDef = 5
        self.startSpeed = 30
        self.startMana = 100
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "def": 2}
        self.boots = { "name": "Bottes en Cuir", "speed": 2 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 2 }
        self.exp = 0
        self.limitExp = 50
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.gold = 0
        self.currentPV = self.startPV
        self.currentDef = self.startDef + self.armor["def"]
        self.currentSpeed = self.startSpeed + self.boots["speed"]
        self.currentDMG = self.startDMG + self.weapon["dmg"]
        
    def getStats(self):
        print(f"Votre personnage a :\n\n- {self.currentPV} PV ({self.startPV} de base)\n- {self.currentDef} DEF ({self.startDef} de base)\n- {self.currentSpeed} SPEED ({self.startSpeed} de base)\n- {self.currentDMG} DMG ({self.startDMG} de base)\n- {self.startMana} de mana")
        return
    
    def getInventory(self):
        print(f"Votre personnage a :\n\n- Armure : {self.armor['name']} (+{self.armor['def']} DEF)\n- Bottes : {self.boots['name']} (+{self.boots['speed']} SPEED)\n- Arme : {self.weapon['name']} (+{self.weapon['dmg']} DMG)\n\n- Potion(s) de soin : {self.items['PotionSoin']}\n- Potion(s) de mana : {self.items['PotionMana']}\n\nVous avez {self.gold} PO et vous êtes level {self.lvl} ({self.exp} exp / {self.limitExp} exp)")
        return
    
    def calculateStats(self):
        self.currentPV = self.startPV
        self.currentDef = self.startDef + self.armor["def"]
        self.currentSpeed = self.startSpeed + self.boots["speed"]
        self.currentDMG = self.startDMG + self.weapon["dmg"]
        return
    
    def resetCharacter(self):
        self.items = { "PotionSoin": 2, "PotionMana": 2}
        self.armor = { "name": "Tunique en Cuire", "def": 2}
        self.boots = { "name": "Bottes en Cuir", "speed": 2 }
        self.weapon = { "name": "Branche d'Arbre", "dmg": 2 }
        self.exp = 0
        self.limitExp = 50
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.gold = 0
        self.calculateStats()
            

character = character()

listeMonstre=["Zombie","Squelette","Brigand","Araignée","Goblin","Loup-Garou","Sirène maléfique","Gnome maléfique"]

class monstres:
    def __init__(self):
        self.type=listeMonstre[random.randint(0,len(listeMonstre)-1)]
        self.lvl = 1
        self.pv = 95
        self.attack = 4
        self.defence = 6
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
        self.lvl = self.lvl
        self.pv = self.pv
        self.attack = self.attack
        self.defence = self.defence
        self.speed = self.speed
        self.currentPV = self.pv
        self.currentDef = self.defence
        self.currentSpeed = self.speed
        self.currentDMG = self.attack
        self.boss = False
        chanceBoss = random.randint(1,100)
        
        if (chanceBoss <= 20) and (character.room > 1):
            self.boss = True
        
    def getStats(self):
        print(f"Le monstre à :\n\n- {self.currentPV} PV ({self.pv} de base)\n- {self.currentDef} DEF ({self.defence} de base)\n- {self.currentSpeed} SPEED ({self.speed} de base)\n- {self.currentDMG} DMG ({self.attack} de base)")
        return

monstre = monstres()

def rarityPicker():
    chance = random.randint(1, 100)
    if 35 <= chance <= 100:
        return listItemsCommon
    elif 10 <= chance < 35:
        return listItemsRare
    elif 5 < chance < 10:
        return listItemsEpic
    elif 1 < chance < 5:
        return listItemsLegendary
    elif chance == 1:
        return listItemsMythic

def shop():
    rarities=[]
    while len(rarities) != 3:
        chancesRarities = random.randint(1, 100)
        if 1 <= chancesRarities <= 25:
            rarities.append(listRarities[2])
        else:
            rarities.append(listRarities[random.randint(0, 1)])
    vente=[rarities[0][random.randint(0,len(rarities[0])-1)],rarities[1][random.randint(0,len(rarities[1])-1)],rarities[1][random.randint(0,len(rarities[2])-1)]]
    character.items["PotionSoin"] = character.items["PotionSoin"] + 2
    character.items["PotionMana"] = character.items["PotionMana"] + 2
    choix = input(f"\n--------------------------------\n\nVous entrez dans une salle dans laquelle le marchand vous donne par gratitude de vos exploits, il vous donne en récompense 2 potions de soins et de mana.\nIl est prêt à vous vendre uniquement 1 de ses 3 items afin de vous aider dans votre quête :\n\n1) {vente[0]['name']} (+{vente[0]['stat']} {vente[0]['type']} prix : {vente[0]['prix']} PO)\n2) {vente[1]['name']} (+{vente[1]['stat']} {vente[1]['type']} prix : {vente[1]['prix']} PO)\n3) {vente[2]['name']} (+{vente[2]['stat']} {vente[2]['type']} prix : {vente[2]['prix']} PO)\n\nVous possédez {character.gold} PO (écrivez le numéro de l'item que vous souhaitez acheter ou bien écrivez \"pass\" pour passer à la prochaine salle): ")
    if choix == '1':
        item = vente[0]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["dmg"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["def"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["speed"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop()
    elif choix == "2":
        item = vente[1]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["dmg"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["def"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["speed"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop()
    elif choix == "3":
        item = vente[2]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["dmg"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["def"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["speed"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop()
    elif choix == "pass":
        print(f"\n--------------------------------\n\nVous avez acheté un/e {vente[int(choix) - 1]['name']}, la salle se fait soudainement envahir par les ténèbres puis après quelques secondes, cette dernière revient à la normale cependant, il ne reste plus que vous !")
        return
    else:
        return shop()
    character.gold = character.gold - vente[int(choix) - 1]['prix']
    character.calculateStats()
    print(f"\n--------------------------------\n\nVous avez acheté un/e {vente[int(choix) - 1]['name']} pour {vente[int(choix) - 1]['prix']} PO, la salle se fait soudainement envahir par les ténèbres puis après quelques secondes, cette dernière revient à la normale cependant, il ne reste plus que vous !")
    return

class tour:
    def __init__(self):
        self.length = 0
        self.TypeTurn = None
        
rounds = tour()
        
def askPlayer():
    question = input("\n--------------------------------\n\nQuelle action voulez-vous réaliser ?\n\n1) attaque\n2) potion\n3) stats\n4) monstre\n5) inventaire\n\nVeuillez indiquer le numéro de l'action que vous souhaitez réaliser : ")
    
    if question == "5":
        print("\n--------------------------------\n")
        character.getInventory()
        time.sleep(3)
        return askPlayer()
    elif question == "1":
        return characterAttacks()
    elif question == "4":
        print("\n--------------------------------\n")
        monstre.getStats()
        time.sleep(3)
        return askPlayer()
    elif question == "3":
        print("\n--------------------------------\n")
        character.getStats()
        time.sleep(3)
        return askPlayer()
    elif question == "2":
        whichPotion = input(f"\n--------------------------------\n\nQuelle potion voulez-vous utiliser ? \nLes potions remplissent entièrement votre vie ou votre mana\n1:vie\n2:mana\n\nVous possédez {character.items['PotionSoin']} potion(s) de soin et {character.items['PotionMana']} potion(s) de mana\nPour retourner en arrière, appuyez sur Entrée : ")
        if whichPotion == "1":
            if character.currentPV == character.startPV:
                print("\n--------------------------------\n\nVotre vie est déjà pleine !")
                return askPlayer()
            character.items["PotionSoin"] = character.items["PotionSoin"] - 1
            character.currentPV = character.startPV
            print(f"\n--------------------------------\n\nVous avez récupéré tous vos PV !")
            return askPlayer()
        elif whichPotion == "2":
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
    randomDMG = random.randint(10, 30)
    DMG = round(randomDMG + character.currentDMG - monstre.currentDef / 2, 0)
    monstre.currentPV = round(monstre.currentPV - DMG, 0)
    if monstre.currentPV <= 0:
        nbrPO = random.randint(50, 200)
        nbrEXP = random.randint(50, 75)
        if monstre.boss == True:
            nbrPO = nbrPO * 2
            nbrEXP = nbrEXP * 2
        print(f"\n--------------------------------\n\n\033[94m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\n{monstre.type} s'est pris \033[91m{DMG}\033[0m DMG ({DMG - character.currentDMG + monstre.currentDef} DMG + {character.currentDMG} DMG - {monstre.currentDef / 2} DEF)\nIl se désintégre sous vous yeux ! (Vous avez reçu {nbrPO} PO et {nbrEXP} points d'exp)\n")
        character.gold = character.gold + nbrPO * monstre.lvl
        character.exp = character.exp + nbrEXP * monstre.lvl
        if character.exp >= character.limitExp:
            while character.exp >= character.limitExp:
                character.lvl = character.lvl + 1
                character.exp = character.exp - character.limitExp
                character.limitExp = character.limitExp + 50
                character.startPV = character.startPV + 2 * character.lvl
                character.startDMG = character.startDMG + 2 * character.lvl
                character.startDef = character.startDef + 2 * character.lvl
                character.startSpeed = character.startSpeed + 2 * character.lvl
                character.calculateStats()
                print(f"--------------------------------\n\n🎉 Félicitations !\nVous êtes monté au niveau supérieur ! ({character.lvl - 1} -> {character.lvl} ({character.exp} exp / {character.limitExp} exp)\nVos stats ont été mises à jour !\n")
        print(f"--------------------------------\n\nVous avez triomphé du mal, cependant il vous reste du chemin à parcourir...\n")
        if monstre.boss==True:
            rarete=rarityPicker()
            item=rarete[random.randint(0,len(rarete)-1)]
            print(item)
            if item["type"]=="dmg":
                character.weapon=item
            if item["type"]=="def":
                character.armor=item
            if item["type"]=="speed":
                character.boots=item
            print("--------------------------------")
            print(f"Un coffre apparait dans le fond de la salle, vous l'ouvrez et trouvez {item['name']} ({item['stat']} {item['type']})")
        reAsk()
    else:
        print(f"\n--------------------------------\n\n\033[94m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\nLe/La/L' {monstre.type} s'est pris \033[91m{DMG}\033[0m DMG ({DMG - character.currentDMG + monstre.currentDef} DMG + {character.currentDMG} DMG - {monstre.currentDef / 2} DEF)\nIl lui reste \033[92m{monstre.currentPV}\033[0m PV !")
        time.sleep(1)
        monstreAttacks()


def monstreAttacks():
    rounds.TypeTurn = "💀"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(10, 30)
    DMG = round(randomDMG + monstre.currentDMG - character.currentDef / 2, 0)
    character.currentPV = round(character.currentPV - DMG, 0)
    if character.currentPV <= 0:
        print(f"\n--------------------------------\n\n\033[91m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :'\033[0m\nVous vous êtes pris \033[91m{DMG}\033[0m DMG ({DMG - monstre.currentDMG + character.currentDef} DMG + {monstre.currentDMG} DMG - {character.currentDef / 2} DEF)\nVous n'êtes plus en état de vous battre !")
        print(f"--------------------------------\n\nLe mal a eu raison de vous...\nIl ne lui restait plus que {monstre.currentPV} PV\n")
        reAskGameOver()
    else:
        print(f"\n--------------------------------\n\n\033[91m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\nVous vous êtes pris \033[91m{DMG}\033[0m DMG ({DMG - monstre.currentDMG + character.currentDef} DMG + {monstre.currentDMG} DMG - {character.currentDef / 2} DEF)\nIl vous reste \033[92m{character.currentPV}\033[0m PV !")
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
    if character.room % 5 == 0:
        print("\n--------------------------------\n\nDès lors que vous vous approchez de la prochaine salle, vous entendez l'entité poussé un bruit résonnant dans tout le donjon !\nCela signifie que ses soldats ont gagnés en puissance, prenez garde !")
        monstre.pv = round(monstre.pv + monstre.pv * 15/100, 0)
        monstre.attack = monstre.attack * 2 + 6
        monstre.speed = round(monstre.speed + monstre.speed * 20/100, 0)
        monstre.defence = monstre.defence * 2 + 2
        monstre.lvl = monstre.lvl + 1
        shop()
        character.room = character.room + 1
    else:
        if character.room != 1:
            monstre.resetMonstre()
        print(f"\n--------------------------------\n\nVous vous approchez d'une porte en bois avec le chiffre \"{character.room}\" insrit dessus, vous l'ouvrez et...\nUn/e {monstre.type} apparaît !")
        rounds.length = 0
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
                print(f"--------------------------------\n\n\033[91m⚠️ Un boss est aparu ! ⚠\033[0m\n")
                monstre.getStats()
        while monstre.currentPV >= 0 and character.currentPV >= 0:
            if monstre.currentSpeed < character.currentSpeed:
                askPlayer()
            else:
                monstreAttacks()

def launchGame():
    rounds.length = 0
    monstre.resetMonstre()
    character.resetCharacter()
    print("-----------------------\n \nVous vous réveillez sans aucun souvenir de la veille dans un recoin sombre d'une pièce froide et lugubre.")
    while game == True:
        launchRoom()
                  
def askTuto():
    tuto = input("tuto ? (y/n) : ")

    if tuto == "y":
        print("Cher joueur, vous allez découvrir un jeux codé grâce aux connaissances acquises en spé N.S.I :\n-----------------------\nLe jeu se joue avec la console de Thonny et est uniquement textuel suivez les instructions et profitez du jeu !\n----------------------- ")
        input("Appuyez sur entrée quand vous êtes prêt !")
        launchGame()
    elif tuto == "n":
        launchGame()
    else:
        askTuto()

askTuto()
