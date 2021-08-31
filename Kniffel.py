#Authors: James King, Sven Krueger
#24.08.21
#Version 1 

import random

class Game:
	__init__(self, numberOfPlayers):
		self.numberOfPlayers = numberOfPlayers
		self.registered = []
		self.roundCounter = 0
		self.playerTurn = 0
	
	for i in self.numberOfPlayers:
		name = input("Name Spieler " + i + ":")
		self.registered[i] = Table(name)
	
	for j in range(13):
		for i in self.numberOfPlayers:
			rolled = Dice()
			possibilities = Table(self.registered[i].name)
			possibilities.table["Einser"] = rolled.numberOf[1] * 1
			possibilities.table["Zweier"] = rolled.numberOf[2] * 2
			possibilities.table["Dreier"] = rolled.numberOf[3] * 3
			possibilities.table["Vierer"] = rolled.numberOf[4] * 4
			possibilities.table["Fünfer"] = rolled.numberOf[5] * 5
			possibilities.table["Sechser"] = rolled.numberOf[6] * 6
			
			possibilities.table["Dreierpasch"] = rolled.checkDreierpasch()[1]
			
		
class Table:
	__init__(self, name):
		self.name = name
		self.table = {"Einser": None, "Zweier": None, "Dreier": None, "Vierer": None, "Fünfer": None, "Sechser": None, "Bonus": None,
			      "Dreierpasch": None, "Viererpasch": None, "FullHouse": None, "KleineStrasse": None, "GrosseStrasse": None, "Kniffel": None, "Chance": None}
	
class Dice:
	
	def bubblesort(roll):
	#Einfacher kurzer Sortieralgorithmus
    		for j in range(5, 0, -1):
        		for i in range(j):
            			if roll[i] > roll[i+1]:
                			x = roll[i]
                			roll[i] = roll[i+1]
                			roll[i+1] = x
                
    		return roll
	
	__init__(self):
		self.roll = bubblesort([random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7)])
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
		
	def chooseDice(roll, chosenIndices):
	#Mit vom Nutzer übergebenen Indices werden die Würfel, die er auswählen will, in einem neuen Array abgespeichert
		chosenDice = []
		for i in chosenIndices:
			chosenDice.append(roll[i])
		return chosenDice
