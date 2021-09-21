import random

class Player:
	def __init__(self, name):
		self.name = name               #Name des Spielers
		self.registered = Table()	   #Tabelle der Punkte des Spielers
		self.bonusAchieved = False	   #zeigt an, ob der Spieler den Bonus schon erreicht hat
		self.sumOfAllPoints = 0		   #Summe aller Punkte des Spielers
	
	def register(self, chosen, points):
		self.registered.table[chosen] = points  #trägt die Punkte an entsprechender Stelle in die Tabelle des Spielers ein
		self.sumOfAllPoints += points			#aktualisiert die Gesamtpunktzahl

class Game:
	def __init__(self, numberOfPlayers):
		self.numberOfPlayers = numberOfPlayers			#Anzahl aller Spieler
		self.players = self.numberOfPlayers * [None]    #Liste aller Spieler
		self.playingPlayer = None		#Der gerade spielende Spieler
		self.playerRollCounter = 0		#Gibt an, in welchem seiner 3 möglichen Würfe sich ein Spieler befindet

	def play(self):
		for i in range(self.numberOfPlayers):
			name = input(f"Name Spieler {i}: ")   #Namensabfrage der Spieler
			self.players[i] = Player(name)		  #Spieler wird erstellt
			
		for roundCounter in range(15):	#es werden insgesamt 15 Runden gespielt
			for i in range(self.numberOfPlayers):	#pro Runde ist jeder Spieler einmal dran			
				self.playingPlayer = self.players[i] #Der Spieler, der gerade an der Reihe ist, wird ausgegeben
				print(self.playingPlayer.name)
			
				rolled = Dice()					 #es wird gewürfelt, ...
				self.playerRollCounter += 1		 #... also wird der Zähler um 1 nach oben gesetzt
				print("Ihr Wurf:", rolled.roll)  #Zeige dem Benutzer seinen Wurf
			
			
				while self.playerRollCounter < 3: #man darf maximal 3 mal würfeln
					continue_ = input("Wollen Sie nochmal würfeln? y/n: ") #kurze Abfrage, ob der Spieler nochmal würfeln will
					if continue_ == "n": #falls der Spieler nicht nochmal würfeln will
						break
					else: #falls der Spieler nochmal würfeln will
						chosenIndices = list(input("Welche Würfel wollen Sie nochmal werfen? (Indizes ohne Leerzeichen eingeben) ")) #Abfrage, welche Würfel nochmal gewürfelt werden sollen
						for k in range(len(chosenIndices)):
							chosenIndices[k] = int(chosenIndices[k])	#Die strings in ints umwandeln 
						rolled.newRoll(chosenIndices)                   #nochmal würfeln, ...
						self.playerRollCounter += 1						#... also wird der Zähler um 1 nach oben gesetzt
						print("Ihr Wurf:", rolled.roll)  				#Zeige dem Benutzer seinen Wurf

				possibilities = Table()			#Diese Tabelle gibt dem Spieler an, welche Punktzahlen er sich eintragen lassen kann
				possibilities.table["Einser"] = rolled.numberOf[1] * 1
				possibilities.table["Zweier"] = rolled.numberOf[2] * 2
				possibilities.table["Dreier"] = rolled.numberOf[3] * 3
				possibilities.table["Vierer"] = rolled.numberOf[4] * 4
				possibilities.table["Fünfer"] = rolled.numberOf[5] * 5
				possibilities.table["Sechser"] = rolled.numberOf[6] * 6
			
				possibilities.table["Dreierpasch"] = rolled.checkDreierpasch()[1]
				possibilities.table["Viererpasch"] = rolled.checkViererpasch()[1]
				possibilities.table["Zweierpasch"] = rolled.checkZweierpasch()[1]
				possibilities.table["DoppelterZweierpasch"] = rolled.checkDoppelterZweierpasch()[1]
				possibilities.table["FullHouse"] = rolled.checkFullHouse()[1]
				possibilities.table["KleineStrasse"] = rolled.checkKleineStrasse()[1]
				possibilities.table["GrosseStrasse"] = rolled.checkGrosseStrasse()[1]
				possibilities.table["Kniffel"] = rolled.checkKniffel()[1]
				possibilities.table["Chance"] = rolled.checkChance()[1]
				
				#Hier werden alle Möglichkeiten ausgegeben, die der Spieler hat, etwas einzutragen.
				for figur in self.playingPlayer.registered.table:
					if self.playingPlayer.registered.table[figur] is None:
						print(figur, possibilities.table[figur])
				

				#Abfrage an den Spieler, was er eintragen will.
				chosen = input("Was wollen Sie eintragen? ")
				while (chosen not in self.playingPlayer.registered.table) or (self.playingPlayer.registered.table[chosen] is not None):      
					chosen = input("Falsche Eingabe. Was wollen Sie eintragen? ") #nochmal fragen, falls der Spieler etwas eintragen will, was nicht geht
				self.playingPlayer.register(chosen, possibilities.table[chosen])  #eintragen, was der Spieler will
				
				#Bonusabfrage
				if self.playingPlayer.registered.checkBonus() and not self.playingPlayer.bonusAchieved:
					self.playingPlayer.bonusAchieved = True
					print("Sie haben den Bonus erreicht")
					self.playingPlayer.registered.table["Bonus"] = 35
					self.playingPlayer.sumOfAllPoints += 35
				
				self.playerRollCounter = 0	#für den nächsten Spieler den Zähler wieder auf 0 setzen
			for player in self.players:
				print(player.name, player.registered.table)    #Ausgabe aller Punktetabellen nach jeder fertigen Runde.
		for player in self.players:
			print(player.name, player.sumOfAllPoints)          #Ausgabe des Gesamtpunktestandes am Ende des Spiels
				
					
class Table:
	def __init__(self):
		#Tabelle der Punktzahlen wird durch ein Dictionary repräsentiert
		self.table = {"Einser": None, "Zweier": None, "Dreier": None, "Vierer": None, "Fünfer": None, "Sechser": None, "Bonus": 0,
			      "Dreierpasch": None, "Viererpasch": None, "Zweierpasch": None, "DoppelterZweierpasch": None, "FullHouse": None, "KleineStrasse": None, "GrosseStrasse": None, "Kniffel": None, "Chance": None}

	def checkBonus(self):  #überprüft, ob der Bonus schon erreicht wurde
		sum = 0
		for key in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:  #Obere Punkte werden zusammengerechnet
			sum += (int(0 if self.table[key] is None else self.table[key]))
		return (sum >= 63)

class Dice:
	def __init__(self, testDice=None):
		if testDice is not None:  #falls man den Wurf manuell setzen will
			self.roll = testDice
		else:					  #sonst zufällige Zahlen für die 5 Würfel
			self.roll = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
		self.numberOf = {1:self.roll.count(1), 2:self.roll.count(2), 3:self.roll.count(3), 4:self.roll.count(4), 5:self.roll.count(5), 6:self.roll.count(6)}
								  #Anzahl 1er, 2er, 3er, 4er, 5er, 6er des Wurfes
		self.sum = sum(self.roll) #Gesamtsumme aller 5 Würfel
	
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

	def checkZweierpasch(self):
	#Überprüft, ob ein Zweierpasch vorliegt
		for i in range(6, 0, -1):
			if self.numberOf[i] >= 2:
				return True, 2*i	#gibt die Summe des größten Zweierpasches zurück
		return False, 0

	def checkDoppelterZweierpasch(self):
	#Überprüft, ob ein doppelter Zweierpasch vorliegt
		counter = 0		#Zählt die Zweierpaschs
		result = 0		#Zählt die Punkte
		for i in range(1, 7):
			if self.numberOf[i] == 2 or self.numberOf[i] == 3:		#Zweier- und Dreierpaschs werden als ein Zweierpasch gezählt
				counter += 1
				result += 2*i
			elif self.numberOf[i] >= 4:								#Viererpaschs und Kniffel werden als zwei Zweierpaschs gezählt
				counter += 2
				result += 4*i
		if counter >= 2:
			return True, result
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
			if self.numberOf[i] >= 2:      		  #für eine große Straße benötigt man 5 verschiedene Zahlen, d.h. es darf keine Zahl mehrmals vorkommen
				return False, 0
		
		if self.numberOf[1] == self.numberOf[6]:  #gibt es sowohl eine 1 als auch eine 6, so kann ebenfalls keine große Straße vorliegen
			return False, 0
		else:									  #nur in allen anderen Fällen liegt eine große Straße vor
			return True, 40
	
	def checkKniffel(self):
	#Überprüft, ob ein Kniffel vorliegt
		if 5 in self.numberOf.values():
			return True, 50
		else:
			return False, 0
		
	def checkChance(self):
	#gibt die Summe aller Würfel zurück
		return True, self.sum
		
	def newRoll(self, chosenIndices):
	#Hier wird nochmal gewürfelt
	#In chosenIndices stehen die Würfel in einer Liste, die der Nutzer nochmal neu werfen will	
		for i in chosenIndices:
			self.roll[i] = random.randint(1,6)
		#Aktualisiere die Attribute numberOf und sum	
		self.numberOf = {1:self.roll.count(1), 2:self.roll.count(2), 3:self.roll.count(3), 4:self.roll.count(4), 5:self.roll.count(5), 6:self.roll.count(6)}	
		self.sum = sum(self.roll)
	

if __name__ == "__main__":
	N = int(input("Anzahl der Spieler: "))
	kniffel = Game(N)
	kniffel.play()
