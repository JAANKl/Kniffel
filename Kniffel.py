#Authors: James King, Sven Krueger
#24.08.21
#Version 0 test

import random

class Game:
	__init__(self):
		registered = {}

class Dice:
	
	def bubblesort(roll):
	#Einfacher kurzer Sortieralgorhythmus
    		for j in range(5, 0, -1):
        		for i in range(j):
            			if roll[i] > roll[i+1]:
                		x = roll[i]
                		roll[i] = roll[i+1]
                		roll[i+1] = x
                
    	return roll
	
	__init__(self):
		self.roll = bubblesort([random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7), random.randint(1,7)])
		self.numberOf = {}
		self.sum = 0
	
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
		if (3 in self.numberOf.values() and 2 in self.numberOf.values()) or 5 in self.numberOf.values():
			return True, 25
		else:
			return False, 0
	
	def checkKleineStrasse(self):
		pass
	
	def checkGrosseStrasse(self):
		pass
	
	def checkKniffel(self):
		if 5 in self.numberOf.values():
			return True
		else:
			return False
