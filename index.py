import random
import time

version = "1.0.0"

game = True

listItemsCommon = [{'name':'Baton', 'stat' : 5, 'prix' : 300, 'type' : 'dmg'},{'name': 'Épée rouillée', 'stat': 5, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Bouclier en bois', 'stat': 4, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Chaussures usées', 'stat': 3, 'prix': 300, 'type': 'speed', 'rarety': 'Common'}, {'name': 'Dague émoussée', 'stat': 6, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Cuirasse légère', 'stat': 7, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Gants en tissu', 'stat': 3, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Sandales en cuir', 'stat': 4, 'prix': 300, 'type': 'speed', 'rarety': 'Common'}, {'name': 'Hache de pierre', 'stat': 5, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Casque cabossé', 'stat': 6, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Arc en bois', 'stat': 4, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Cape usée', 'stat': 2, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Sceptre basique', 'stat': 5, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Bottes de marche', 'stat': 4, 'prix': 300, 'type': 'speed', 'rarety': 'Common'}, {'name': 'Gants en cuir', 'stat': 3, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Armure légère', 'stat': 6, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Pantalon renforcé', 'stat': 5, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Hache de fer', 'stat': 7, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Chapeau en cuir', 'stat': 4, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Fléau léger', 'stat': 6, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Targe en bois', 'stat': 5, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Couteau de chasse', 'stat': 4, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Chaussures de lin', 'stat': 3, 'prix': 300, 'type': 'speed', 'rarety': 'Common'}, {'name': 'Épée courte', 'stat': 5, 'prix': 300, 'type': 'dmg', 'rarety': 'Common'}, {'name': 'Casque en fer', 'stat': 6, 'prix': 300, 'type': 'def', 'rarety': 'Common'}, {'name': 'Bouclier léger', 'stat': 5, 'prix': 300, 'type': 'def', 'rarety': 'Common'}]
listItemsRare = [{'name':'Bottes Symbiotiques', 'stat' : 10, 'prix': 700, 'type' : 'speed'},{'name': 'Bottes de vitesse', 'stat': 10, 'prix': 700, 'type': 'speed', 'rarety': 'Rare'},{'name': 'Épée aiguisée', 'stat': 12, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Bouclier renforcé', 'stat': 10, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Chaussures en cuir renforcé', 'stat': 8, 'prix': 700, 'type': 'speed', 'rarety': 'Rare'}, {'name': 'Dague acérée', 'stat': 11, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Cuirasse d’acier', 'stat': 13, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Gants de combat', 'stat': 9, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Sandales rapides', 'stat': 10, 'prix': 700, 'type': 'speed', 'rarety': 'Rare'}, {'name': 'Hache tranchante', 'stat': 14, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Casque solide', 'stat': 12, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Arc de chasse', 'stat': 9, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Cape renforcée', 'stat': 7, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Sceptre magique', 'stat': 13, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': "Bottes d'agilité", 'stat': 11, 'prix': 700, 'type': 'speed', 'rarety': 'Rare'}, {'name': 'Gants renforcés', 'stat': 10, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Armure lourde', 'stat': 12, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Pantalon en acier', 'stat': 11, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Hache à double tranchant', 'stat': 15, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Chapeau de guerre', 'stat': 9, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Fléau en métal', 'stat': 14, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': 'Targe en acier', 'stat': 11, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Couteau de guerre', 'stat': 10, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': "Chaussures d'aventure", 'stat': 9, 'prix': 700, 'type': 'speed', 'rarety': 'Rare'}, {'name': 'Épée de combat', 'stat': 13, 'prix': 700, 'type': 'dmg', 'rarety': 'Rare'}, {'name': "Casque d'acier", 'stat': 12, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}, {'name': 'Bouclier robuste', 'stat': 11, 'prix': 700, 'type': 'def', 'rarety': 'Rare'}]
listItemsEpic = [{'name':'Coeuracier', 'stat' : 10, 'prix' : 1000, 'type': 'def'},{'name': 'Épée de feu','stat': 15,'prix': 1000,  'type': 'dmg','rarety': 'Epic'},{'name': 'Lame de guerre', 'stat': 20, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Armure de chevalier', 'stat': 18, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Bottes du vent', 'stat': 16, 'prix': 1000, 'type': 'speed', 'rarety': 'Epic'}, {'name': 'Dague venimeuse', 'stat': 19, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Cuirasse royale', 'stat': 22, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Gants de force', 'stat': 17, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Sandales rapides', 'stat': 18, 'prix': 1000, 'type': 'speed', 'rarety': 'Epic'}, {'name': 'Hache de bataille', 'stat': 24, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Casque béni', 'stat': 20, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': "Arc d'élite", 'stat': 21, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Cape dorée', 'stat': 15, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Sceptre du dragon', 'stat': 23, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Bottes de célérité', 'stat': 19, 'prix': 1000, 'type': 'speed', 'rarety': 'Epic'}, {'name': 'Gants mystiques', 'stat': 18, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': "Armure d'acier", 'stat': 20, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Jambières de titan', 'stat': 21, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Hache royale', 'stat': 25, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Chapeau de magicien', 'stat': 17, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Fléau destructeur', 'stat': 22, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Bouclier de feu', 'stat': 19, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': 'Couteau rapide', 'stat': 18, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': 'Chaussures de voyage', 'stat': 17, 'prix': 1000, 'type': 'speed', 'rarety': 'Epic'}, {'name': 'Épée du dragon', 'stat': 23, 'prix': 1000, 'type': 'dmg', 'rarety': 'Epic'}, {'name': "Casque d'acier renforcé", 'stat': 22, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}, {'name': "Bouclier d'élite", 'stat': 20, 'prix': 1000, 'type': 'def', 'rarety': 'Epic'}]
listItemsLegendary = [{'name': 'Bouclier de pierre', 'stat': 20, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'},{'name': 'Épée de légende', 'stat': 30, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Bouclier sacré', 'stat': 28, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Bottes d’éclair', 'stat': 25, 'prix': 2000, 'type': 'speed', 'rarety': 'Legendary'}, {'name': 'Dague mortelle', 'stat': 29, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Cuirasse divine', 'stat': 32, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Gants du destin', 'stat': 26, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Sandales du vent', 'stat': 27, 'prix': 2000, 'type': 'speed', 'rarety': 'Legendary'}, {'name': 'Hache colossale', 'stat': 35, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Casque du roi', 'stat': 30, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Arc mythique', 'stat': 31, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Cape royale', 'stat': 24, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Sceptre des dieux', 'stat': 33, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Bottes célestes', 'stat': 29, 'prix': 2000, 'type': 'speed', 'rarety': 'Legendary'}, {'name': 'Gants de pouvoir', 'stat': 28, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Armure invincible', 'stat': 30, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Jambières de héros', 'stat': 31, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Hache de guerre ultime', 'stat': 36, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Couronne royale', 'stat': 27, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Fléau des titans', 'stat': 32, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': "Bouclier de l'invincible", 'stat': 29, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': "Couteau d'élite", 'stat': 27, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Chaussures de héros', 'stat': 26, 'prix': 2000, 'type': 'speed', 'rarety': 'Legendary'}, {'name': 'Épée céleste', 'stat': 33, 'prix': 2000, 'type': 'dmg', 'rarety': 'Legendary'}, {'name': 'Casque mythique', 'stat': 32, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}, {'name': 'Bouclier royal', 'stat': 30, 'prix': 2000, 'type': 'def', 'rarety': 'Legendary'}]
listItemsMythic = [{'name': 'Épée divine', 'stat': 50, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Armure céleste', 'stat': 45, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Bottes du tonnerre', 'stat': 40, 'prix': 5000, 'type': 'speed', 'rarety': 'Mythic'}, {'name': "Dague de l'ombre", 'stat': 48, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Cuirasse mythique', 'stat': 52, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Gants divins', 'stat': 43, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': "Sandales d'évasion", 'stat': 44, 'prix': 5000, 'type': 'speed', 'rarety': 'Mythic'}, {'name': 'Hache apocalyptique', 'stat': 60, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Casque des dieux', 'stat': 50, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Arc céleste', 'stat': 49, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Cape des ombres', 'stat': 38, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Sceptre du destin', 'stat': 55, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Bottes de vitesse divine', 'stat': 46, 'prix': 5000, 'type': 'speed', 'rarety': 'Mythic'}, {'name': 'Gants du crépuscule', 'stat': 45, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Armure indestructible', 'stat': 48, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Jambières divines', 'stat': 47, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Hache céleste', 'stat': 56, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Casque de titan', 'stat': 44, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Fléau apocalyptique', 'stat': 53, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Bouclier invincible', 'stat': 46, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Couteau des dieux', 'stat': 45, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Chaussures célestes', 'stat': 43, 'prix': 5000, 'type': 'speed', 'rarety': 'Mythic'}, {'name': 'Épée de la lumière', 'stat': 57, 'prix': 5000, 'type': 'dmg', 'rarety': 'Mythic'}, {'name': 'Casque éternel', 'stat': 50, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}, {'name': 'Bouclier mythique', 'stat': 48, 'prix': 5000, 'type': 'def', 'rarety': 'Mythic'}]

listRarities = [listItemsCommon, listItemsRare, listItemsEpic, listItemsLegendary, listItemsMythic]

class character:
    def __init__(self):
        self.startPV = 100
        self.startDMG = 3
        self.startDef = 5
        self.startSpeed = 30
        self.startMana = 100
        self.items = { "PotionSoin": 2 }
        self.armor = { "name": "Tunique en Cuire", "stat": 2}
        self.boots = { "name": "Bottes en Cuir", "stat": 2 }
        self.weapon = { "name": "Branche d'Arbre", "stat": 2 }
        self.exp = 0
        self.limitExp = 50
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.gold = 0
        self.currentPV = self.startPV
        self.currentDef = self.startDef + self.armor["stat"]
        self.currentSpeed = self.startSpeed + self.boots["stat"]
        self.currentDMG = self.startDMG + self.weapon["stat"]
        
    def getStats(self):
        print(f"Votre personnage a :\n\n- {self.currentPV} PV ({self.startPV} de base)\n- {self.currentDef} DEF ({self.startDef} de base)\n- {self.currentSpeed} SPEED ({self.startSpeed} de base)\n- {self.currentDMG} DMG ({self.startDMG} de base)")
        input("--------------------------------\n\nAppuyez sur entrée quand vous êtes prêt...")
        return
    
    def getInventory(self):
        print(f"Votre personnage a :\n\n- Armure : {self.armor['name']} (+{self.armor['stat']} DEF)\n- Bottes : {self.boots['name']} (+{self.boots['stat']} SPEED)\n- Arme : {self.weapon['name']} (+{self.weapon['stat']} DMG)\n\n- Potion(s) de soin : {self.items['PotionSoin']}\n\nVous avez {self.gold} PO et vous êtes level {self.lvl} ({self.exp} exp / {self.limitExp} exp)")
        input("--------------------------------\n\nAppuyez sur entrée quand vous êtes prêt...")
        return
    
    def calculateStats(self):
        self.currentPV = self.startPV
        self.currentDef = self.startDef + self.armor["stat"]
        self.currentSpeed = self.startSpeed + self.boots["stat"]
        self.currentDMG = self.startDMG + self.weapon["stat"]
        return
    
    def resetCharacter(self):
        self.items = { "PotionSoin": 2 }
        self.armor = { "name": "Tunique en Cuire", "stat": 2}
        self.boots = { "name": "Bottes en Cuir", "stat": 2 }
        self.weapon = { "name": "Branche d'Arbre", "stat": 2 }
        self.exp = 0
        self.limitExp = 50
        self.lvl = 1
        self.chests = 0
        self.room = 1
        self.gold = 0
        self.calculateStats()
        return
            

character = character()

listeMonstre=["Un Zombie","Un Squelette","Un Brigand","Une Araignée","Un Goblin","Un Loup-Garou","Une Sirène maléfique","Un Gnome maléfique"]

class monstres:
    def __init__(self):
        self.type=listeMonstre[random.randint(0,len(listeMonstre)-1)]
        self.lvl = 1
        self.pv = 105
        self.attack = 6
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

currentItemsShop = None

def generateShop():
    rarities=[]
    while len(rarities) != 3:
        chancesRarities = random.randint(1, 100)
        if 1 <= chancesRarities <= 25:
            rarities.append(listRarities[2])
        else:
            randomNumber1 = random.randint(0, 1)
            rarities.append(listRarities[randomNumber1])
    vente=[rarities[0][random.randint(0,len(rarities[0])-1)],rarities[1][random.randint(0,len(rarities[1])-1)],rarities[2][random.randint(0,len(rarities[2])-1)]]
    return vente

def shop(ItemsShop):
    vente = ItemsShop
    itemsAvailability = []
    for item in vente:
        if item["prix"] > character.gold:
            itemsAvailability.append(f"\033[91m{item['name']}\033[0m")
        else:
            itemsAvailability.append(f"\033[92m{item['name']}\033[0m")
    choix = input(f"\n--------------------------------\n\nVous entrez dans une salle dans laquelle un marchand nommé M.Barret, en récompense de vos exploits, vous offre 2 potions de soins.\nIl est prêt à vous vendre uniquement 1 de ses 3 items afin de vous aider dans votre quête :\n\n1) {itemsAvailability[0]} (+{vente[0]['stat']} {vente[0]['type']} prix : {vente[0]['prix']} PO)\n2) {itemsAvailability[1]} (+{vente[1]['stat']} {vente[1]['type']} prix : {vente[1]['prix']} PO)\n3) {itemsAvailability[2]} (+{vente[2]['stat']} {vente[2]['type']} prix : {vente[2]['prix']} PO)\n\nVous possédez {character.gold} PO (écrivez le numéro de l'item que vous souhaitez acheter ou bien écrivez \"pass\" pour passer à la prochaine salle): ")
    if choix == '1':
        item = vente[0]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["stat"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["stat"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["stat"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop(ItemsShop)
    elif choix == "2":
        item = vente[1]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["stat"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["stat"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["stat"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop(ItemsShop)
    elif choix == "3":
        item = vente[2]
        if character.gold >= item['prix']:
            if item["type"] == "dmg":
                character.weapon["name"] = item["name"]
                character.weapon["stat"] = item["stat"]
            elif item["type"] == "def":
                character.armor["name"] = item["name"]
                character.armor["stat"] = item["stat"]
            elif item["type"] == "speed":
                character.boots["name"] = item["name"]
                character.boots["stat"] = item["stat"]
        else:
            print("\n--------------------------------\n\nVous n'avez pas assez de PO !\n--------------------------------")
            return shop(ItemsShop)
    elif choix == "pass":
        print(f"\n--------------------------------\n\nLa salle se fait soudainement envahir par les ténèbres puis après quelques secondes, cette dernière revient à la normale cependant, il ne reste plus que vous !")
        return
    else:
        return shop(ItemsShop)
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
    question = input(f"\n--------------------------------\n\nQuelle action voulez-vous réaliser ?\n\n1) attaque\n2) potion\n3) stats\n4) monstre\n5) inventaire\n\nVous avez:\n\n{character.currentPV} PV | {character.currentDMG} DMG | {character.currentDef} DEF | {character.currentSpeed} SPEED\n\nVeuillez marquer le numéro de l'action que vous souhaitez réaliser : ")
    
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
        if character.currentPV == character.startPV:
            print("\n--------------------------------\n\nVotre vie est déjà pleine !")
            time.sleep(3)
            return askPlayer()
        questionPotion = input(f'\n--------------------------------\n\nVous possédez {character.items["PotionSoin"]} potions de soin et il vous reste {character.currentPV} PV\nSouhaitez-vous utiliser une potion pour retrouver toute votre santé (y/n) :')
        if questionPotion.lower() == "y":
            character.items["PotionSoin"] = character.items["PotionSoin"] - 1
            oldPV = character.currentPV
            character.currentPV = character.startPV
            print(f"\n--------------------------------\n\nVous avez récupéré tous vos PV ! ({oldPV} PV ---> {character.currentPV} PV)")
            time.sleep(3)
            return askPlayer()
        else:
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
        nbrPO = random.randint(100, 250) * monstre.lvl
        nbrEXP = random.randint(50, 75) * monstre.lvl
        if monstre.boss == True:
            nbrPO = nbrPO * 2
            nbrEXP = nbrEXP * 2
        print(f"\n--------------------------------\n\n\033[94m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\n{monstre.type} s'est pris \033[91m{DMG}\033[0m Dégats\nIl se désintégre sous vous yeux ! (Vous avez reçu {nbrPO} PO et {nbrEXP} points d'exp)\n")
        time.sleep(1)
        print(f"--------------------------------\n\nVous avez triomphé du mal, cependant il vous reste du chemin à parcourir...\n")
        character.gold = character.gold + nbrPO
        character.exp = character.exp + nbrEXP
        if character.exp >= character.limitExp:
            while character.exp >= character.limitExp:
                oldStatsPlayer = { "PV": character.currentPV, "DMG": character.currentDMG, "DEF": character.currentDef, "SPEED": character.currentSpeed }
                character.lvl = character.lvl + 1
                character.exp = character.exp - character.limitExp
                character.limitExp = character.limitExp + 50
                character.startPV = round(character.startPV + 3 + 35/100 * character.lvl, 0)
                character.startDMG = round(character.startDMG + 3 + 25/100 * character.lvl, 0)
                character.startDef = round(character.startDef + 3 + 15/100 * character.lvl, 0)
                character.startSpeed = round(character.startSpeed + 3 + 20/100 * character.lvl, 0)
                character.calculateStats()
                print(f'--------------------------------\n\n🎉 Félicitations !\nVous êtes monté au niveau supérieur ! ({character.lvl - 1} -> {character.lvl} ({character.exp} exp / {character.limitExp} exp)\n\nVos stats ont été mises à jour :\n\n- {oldStatsPlayer["PV"]} PV --> {character.currentPV} PV\n- {oldStatsPlayer["DMG"]} DMG --> {character.currentDMG} DMG\n- {oldStatsPlayer["DEF"]} DEF --> {character.currentDef} DEF\n- {oldStatsPlayer["SPEED"]} SPEED --> {character.currentSpeed} SPEED\n')
                time.sleep(2)
        if monstre.boss==True:
            rarete=rarityPicker()
            item=rarete[random.randint(0, len(rarete))]
            if item["type"]=="dmg":
                character.weapon=item
            if item["type"]=="def":
                character.armor=item
            if item["type"]=="speed":
                character.boots=item
            print("--------------------------------")
            print(f"\nUn coffre apparait dans le fond de la salle, vous l'ouvrez et trouvez {item['name']} ({item['stat']} {item['type'].upper()})\n")
        input("--------------------------------\n\nAppuyez sur entrée quand vous êtes prêt...")
        character.room = character.room + 1
        return launchRoom()
    else:
        print(f"\n--------------------------------\n\n\033[94m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\n{monstre.type} s'est pris \033[91m{DMG}\033[0m Dégats\nIl lui reste \033[92m{monstre.currentPV}\033[0m PV !")
        time.sleep(1.3)
        monstreAttacks()


def monstreAttacks():
    rounds.TypeTurn = "💀"
    rounds.length = rounds.length + 1
    randomDMG = random.randint(10, 30)
    DMG = round(randomDMG + monstre.currentDMG - character.currentDef / 2, 0)
    character.currentPV = round(character.currentPV - DMG, 0)
    if character.currentPV <= 0:
        print(f"\n--------------------------------\n\n\033[91m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :'\033[0m\nVous vous êtes pris \033[91m{DMG}\033[0m Dégats \nVous n'êtes plus en état de vous battre !")
        print(f"--------------------------------\n\nLe mal a eu raison de vous...\nIl ne lui restait plus que {monstre.currentPV} PV\n")
        time.sleep(1)
        reAskGameOver()
    else:
        print(f"\n--------------------------------\n\n\033[91m{rounds.TypeTurn} Round {rounds.length} | Salle n°{character.room} :\033[0m\nVous vous êtes pris \033[91m{DMG}\033[0m Dégats\nIl vous reste \033[92m{character.currentPV}\033[0m PV !")
        time.sleep(2)
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
        

def launchRoom():
    if character.room % 5 == 0:
        print("\n--------------------------------\n\nDès lors que vous vous approchez de la prochaine salle, vous entendez l'entité poussé un bruit résonnant dans tout le donjon !\nLa légende raconte que ce cri permet à ses soldats de gagner en puissance, prenez garde !")
        time.sleep(2)
        monstre.pv = round(monstre.pv + monstre.pv * 15/100, 0)
        monstre.attack = round(monstre.attack + 4 + monstre.lvl * 25/100, 0)
        monstre.speed = round(monstre.speed + monstre.speed * 20/100, 0)
        monstre.defence = round(monstre.defence + 6 + monstre.lvl * 25/100, 0)
        monstre.lvl = monstre.lvl + 1
        currentItemsShop = generateShop()
        character.items["PotionSoin"] = character.items["PotionSoin"] + 2
        shop(currentItemsShop)
        character.room = character.room + 1
    else:
        if character.room != 1:
            monstre.resetMonstre()
        print(f"\n--------------------------------\n\nVous vous approchez d'une porte en bois avec le chiffre \"{character.room}\" insrit dessus, vous l'ouvrez et...\nUn/e {monstre.type} apparaît !")
        time.sleep(1.3)
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
                print(f"--------------------------------\n\n\033[91m⚠ Un boss est aparu ! ⚠\033[0m\n")
                monstre.getStats()
                time.sleep(2)
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
    time.sleep(3)
    while game == True:
        launchRoom()
                  
def askTuto():

    print(("""\033[91m
 _____                   _             _    _   _             _            
|_   _|                 (_)           | |  | | | |           | |           
  | | ___ _ __ _ __ ___  _ _ __   __ _| |  | |_| |_   _ _ __ | |_ ___ _ __ 
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | |  |  _  | | | | '_ \| __/ _ \ '__|
  | |  __/ |  | | | | | | | | | | (_| | |  | | | | |_| | | | | ||  __/ |   
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_|  \_| |_/\__,_|_| |_|\__\___|_|                                                             
\033[0m"""))
    
    print(f"\033[91mv{version}\033[0m\n\n------------------------------------------------------------------------------")
    
    tuto = input("Souhaitez-vous accéder au tutoriel ? (y/n) : ")

    if tuto.lower() == "y":
        print("Cher joueur, vous allez découvrir un jeux codé grâce aux connaissances acquises en spé N.S.I :\n-----------------------\nLe jeu se joue avec la console de Thonny et est uniquement textuel suivez les instructions et profitez du jeu !\n----------------------- ")
        input("Appuyez sur entrée quand vous êtes prêt !")
        launchGame()
    elif tuto.lower() == "n":
        launchGame()
    else:
        askTuto()

askTuto()
