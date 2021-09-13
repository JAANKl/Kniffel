import random

class Player:
	def __init__(self, name):
		self.name = name
		self.registered = Table()
		self.bonusAchieved = False
		self.sumOfAllPoints = 0


class Table:
	def __init__(self):
		self.table = {"Einser": None, "Zweier": None, "Dreier": None, "Vierer": None, "Fünfer": None, "Sechser": None, "Bonus": 0,
			      "Dreierpasch": None, "Viererpasch": None, "FullHouse": None, "KleineStrasse": None, "GrosseStrasse": None, "Kniffel": None, "Chance": None}

	def checkBonus(self):
		sum = 0
		for key in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
			sum += (int(0 if self.table[key] is None else self.table[key]))
		return (sum >= 63)


class Dice:
	
	def __init__(self):
		self.roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
		self.numberOf = {1:self.roll.count(1), 2:self.roll.count(2), 3:self.roll.count(3), 4:self.roll.count(4), 5:self.roll.count(5), 6:self.roll.count(6)}
				#Anzahl 1er, 2er, 3er, 4er, 5er, 6er des Wurfes
		self.sum = sum(self.roll)
	
	def checkDreierpasch(self):
	#Überprüft, ob ein Dreier-, Viererpasch oder Kniffel vorhanden ist.
		if 3 in self.numberOf.values() or 4 in self.numberOf.values() or 5 in self.numberOf.values():
			return True, self.sum
		else:
			return False, 0
	
	def checkViererpasch(self):
	#Überprüft, ob ein Viererpasch oder Kniffel vorhanden ist.
		if 4 in self.numberOf.values() or 5 in self.numberOf.values():
			return True, self.sum
		else:
			return False, 0
	
	def checkFullHouse(self):
	#Überprüft, ob ein Dreierpasch und ein anderer Zweierpasch, oder ob ein Kniffel vorhanden ist.
		if (3 in self.numberOf.values() and 2 in self.numberOf.values()) or 5 in self.numberOf.values():
			return True, 25
		else:
			return False, 0
	
	def checkKleineStrasse(self):
	#Überprüft alle Möglichkeiten einer kleinen Straße (also [1,2,3,4,x], [2,3,4,5,x], [3,4,5,6,x])
		if (1 in self.roll and 2 in self.roll and 3 in self.roll and 4 in self.roll) or (2 in self.roll and 3 in self.roll and 4 in self.roll and 5 in self.roll) or (3 in self.roll and 4 in self.roll and 5 in self.roll and 6 in self.roll):
			return True, 30
		else:
			return False, 0
	
	def checkGrosseStrasse(self):
		for i in range(1,7):
			if self.numberOf[i] >= 2:      #für eine große Straße benötigt man 5 verschiedene Zahlen, d.h. es darf keine Zahl mehrmals vorkommen
				return False, 0
		
		if self.numberOf[1] == self.numberOf[6]:  #gibt es sowohl eine 1 als auch eine 6, so kann ebenfalls keine große Straße vorliegen
			return False, 0
		else:
			return True, 40
	
	def checkKniffel(self):
		if 5 in self.numberOf.values():
			return True, 50
		else:
			return False, 0
		
	def checkChance(self):
		return True, self.sum
		
	def newRoll(self, chosenIndices):
	#In chosenIndices stehen die Würfel in einer Liste, die der Nutzer nochmal neu werfen will	
		for i in chosenIndices:
			self.roll[i] = random.randint(1,6)	
		#Aktualisiere die Attribute numberOf und sum	
		self.numberOf = {1:self.roll.count(1), 2:self.roll.count(2), 3:self.roll.count(3), 4:self.roll.count(4), 5:self.roll.count(5), 6:self.roll.count(6)}	
		self.sum = sum(self.roll)


class Game:
    def __init__(self, numberOfPlayers=1):
        #self.numberOfPlayers = numberOfPlayers
        #self.players = self.numberOfPlayers * [None]    #Liste aller Spieler
        #self.playingPlayer = None   #Name des gerade spielenden Spielers
        self.playerRollCounter = 0  #Gibt an, in welchem seiner 3 möglichen Würfe sich ein Spieler befindet
        self.dice = Dice()
        self.player = Player("Spieler")
        self.roundCounter = 1       #Gibt an, in welcher Runde man sich befindet

    def rollDice(self, chosenIndices, numberOfRolls):
        if numberOfRolls < 3:
            self.dice.newRoll(chosenIndices)
        else:
            raise TooManyRolls("Es wurde schon dreimal gewürfelt")
    
    def possibilities(self):
        possibilities = Table()
        possibilities.table["Einser"] = self.dice.numberOf[1] * 1
        possibilities.table["Zweier"] = self.dice.numberOf[2] * 2
        possibilities.table["Dreier"] = self.dice.numberOf[3] * 3
        possibilities.table["Vierer"] = self.dice.numberOf[4] * 4
        possibilities.table["Fünfer"] = self.dice.numberOf[5] * 5
        possibilities.table["Sechser"] = self.dice.numberOf[6] * 6
		
        possibilities.table["Dreierpasch"] = self.dice.checkDreierpasch()[1]
        possibilities.table["Viererpasch"] = self.dice.checkViererpasch()[1]
        possibilities.table["FullHouse"] = self.dice.checkFullHouse()[1]
        possibilities.table["KleineStrasse"] = self.dice.checkKleineStrasse()[1]
        possibilities.table["GrosseStrasse"] = self.dice.checkGrosseStrasse()[1]
        possibilities.table["Kniffel"] = self.dice.checkKniffel()[1]
        possibilities.table["Chance"] = self.dice.checkChance()[1]
        
        return possibilities
    
    def register(self, figur):
        if self.player.registered.table[figur] is None:
            self.player.registered.table[figur] = self.possibilities().table[figur]
        else:
            raise AlreadyRegistered("Ist bereits eingetragen")

class AlreadyRegistered(Exception):
	pass #Exception, falls man etwas eintragen will, was schon eingetragen wurde

class TooManyRolls(Exception):
	pass #Exception, falls schon zu oft gewürfelt wurde
