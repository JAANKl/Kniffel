#Authors: James King, Sven Krueger
#24.08.21
#Version 0 test

import random

class Game:
	__init__(self):
		registered = {}

class Dice:
	
	def bubblesort():
		pass
	
	__init__(self):
		self.roll = bubblesort([random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7) ])
		self.numberOf = {}
		self.sum = 0
	
	def checkDreierpasch(self):
		pass
	
	def checkViererpasch(self):
		pass
	
	def checkFullHouse(self):
		pass
	
	def checkKleineStrasse(self):
		pass
	
	def checkGrosseStrasse(self):
		for i in range(1,7):
			if self.numberOf[i] >= 2:      #für eine große Straße benötigt man 5 verschiedene Zahlen, d.h. es darf keine Zahl mehrmals vorkommen
				return False
		
		if self.numberOf[1] == self.numberOf[6]:  #gibt es sowohl eine 1 als auch eine 6, so kann ebenfalls keine große Straße vorliegen
			return False
		else:
			return True
		
	
	def checkKniffel(self):
		if 5 in self.numberOf.values():
			return True
		else:
			return False
