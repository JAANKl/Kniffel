#Authors: James King, Sven Krueger
#22.09.21

import unittest
import kniffel_konsole as _logic

class TestKniffel(unittest.TestCase):

    def test_Numbers(self):
    #Tests für das obere Spiel
        testDice = _logic.Dice([1, 3, 3, 4, 6])
        self.assertEqual(testDice.numberOf[1] * 1, 1)
        self.assertEqual(testDice.numberOf[2] * 2, 0)
        self.assertEqual(testDice.numberOf[3] * 3, 6)
        self.assertEqual(testDice.numberOf[4] * 4, 4)
        self.assertEqual(testDice.numberOf[5] * 5, 0)
        self.assertEqual(testDice.numberOf[6] * 6, 6)

        testDice = _logic.Dice([2, 2, 2, 5, 5])
        self.assertEqual(testDice.numberOf[1] * 1, 0)
        self.assertEqual(testDice.numberOf[2] * 2, 6)
        self.assertEqual(testDice.numberOf[3] * 3, 0)
        self.assertEqual(testDice.numberOf[4] * 4, 0)
        self.assertEqual(testDice.numberOf[5] * 5, 10)
        self.assertEqual(testDice.numberOf[6] * 6, 0)

    def test_checkDreierpasch(self):
    #Tests für Dreierpasch
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkDreierpasch()[0])
        self.assertEqual(testDice.checkDreierpasch()[1], 28)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkDreierpasch()[0])
        self.assertEqual(testDice.checkDreierpasch()[1], 0)
    
    def test_checkViererpasch(self):
    #Tests für Viererpasch
        testDice = _logic.Dice([6, 6, 6, 6, 5])
        self.assertTrue(testDice.checkViererpasch()[0])
        self.assertEqual(testDice.checkViererpasch()[1], 29)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkViererpasch()[0])
        self.assertEqual(testDice.checkViererpasch()[1], 0)

    def test_checkZweierpasch(self):
    #Tests für Zweierpasch
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkZweierpasch()[0])
        self.assertEqual(testDice.checkZweierpasch()[1], 12)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkZweierpasch()[0])
        self.assertEqual(testDice.checkZweierpasch()[1], 0)

    def test_checkDoppelterZweierpasch(self):
    #Tests für doppelten Zweierpasch
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkDoppelterZweierpasch()[0])
        self.assertEqual(testDice.checkDoppelterZweierpasch()[1], 22)

        testDice = _logic.Dice([1, 2, 3, 5, 5])
        self.assertFalse(testDice.checkDoppelterZweierpasch()[0])
        self.assertEqual(testDice.checkDoppelterZweierpasch()[1], 0)

        testDice = _logic.Dice([1, 1, 1, 1, 1])
        self.assertTrue(testDice.checkDoppelterZweierpasch()[0])
        self.assertEqual(testDice.checkDoppelterZweierpasch()[1], 4)

    def test_checkFullHouse(self):
    #Tests für Full House
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkFullHouse()[0])
        self.assertEqual(testDice.checkFullHouse()[1], 25)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkFullHouse()[0])
        self.assertEqual(testDice.checkFullHouse()[1], 0)
    
    def test_checkKleineStrasse(self):
    #Tests für Kleine Straße
        testDice = _logic.Dice([1, 2, 3, 4, 2])
        self.assertTrue(testDice.checkKleineStrasse()[0])
        self.assertEqual(testDice.checkKleineStrasse()[1], 30)

        testDice = _logic.Dice([1, 2, 3, 5, 6])
        self.assertFalse(testDice.checkKleineStrasse()[0])
        self.assertEqual(testDice.checkKleineStrasse()[1], 0)
    
    def test_checkGrosseStrasse(self):
    #Tests für Große Straße
        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertTrue(testDice.checkGrosseStrasse()[0])
        self.assertEqual(testDice.checkGrosseStrasse()[1], 40)

        testDice = _logic.Dice([1, 2, 3, 5, 6])
        self.assertFalse(testDice.checkGrosseStrasse()[0])
        self.assertEqual(testDice.checkGrosseStrasse()[1], 0)
    
    def test_checkKniffel(self):
    #Tests für Kniffel
        testDice = _logic.Dice([1, 1, 1, 1, 1])
        self.assertTrue(testDice.checkKniffel()[0])
        self.assertEqual(testDice.checkKniffel()[1], 50)

        testDice = _logic.Dice([1, 1, 1, 1, 2])
        self.assertFalse(testDice.checkKniffel()[0])
        self.assertEqual(testDice.checkKniffel()[1], 0)
    
    def test_checkChance(self):
    #Tests für Chance
        testDice = _logic.Dice([1, 3, 4, 5, 5])
        self.assertTrue(testDice.checkChance()[0])
        self.assertEqual(testDice.checkChance()[1], 18)

        testDice = _logic.Dice([3, 3, 3, 3, 3])
        self.assertTrue(testDice.checkChance()[0])
        self.assertEqual(testDice.checkChance()[1], 15)
    
    def test_register(self):
    #Tests für die Methode register()
        testPlayer = _logic.Player("Test")
        testPlayer.register("GrosseStrasse", 40)
        self.assertEqual(testPlayer.registered.table["GrosseStrasse"], 40)  #überprüfe, ob das richtige eingetragen wurde
        self.assertIsNone(testPlayer.registered.table["Kniffel"])           #überprüfe, ob etwas zufällig ausgewählt Anderes nicht eingetragen wurde
        self.assertEqual(testPlayer.sumOfAllPoints, 40)                     #überprüfe, ob die Gesamtpunktzahl richtig aktualisiert wurde

        testPlayer.register("Sechser", 18)
        self.assertEqual(testPlayer.registered.table["Sechser"], 18)    #überprüfe, ob das richtige eingetragen wurde
        self.assertIsNone(testPlayer.registered.table["Zweier"])        #überprüfe, ob etwas zufällig ausgewählt Anderes nicht eingetragen wurde
        self.assertEqual(testPlayer.sumOfAllPoints, 58)                 #überprüfe, ob die Gesamtpunktzahl richtig aktualisiert wurde
    
    def test_checkBonus(self):
    #Tests für den Bonus
        testTable = _logic.Table()
        #zunächst ein paar Sachen eintragen
        testTable.table["Chance"] = 23
        testTable.table["Einser"] = 3
        testTable.table["Kniffel"] = 50
        testTable.table["Zweier"] = 6
        testTable.table["GrosseStrasse"] = 40
        testTable.table["Dreier"] = 9
        testTable.table["KleineStrasse"] = 30
        self.assertFalse(testTable.checkBonus())    #überprüfe, dass der Bonus nicht schon eingetragen wird, wenn man zwar insgesamt schon mehr als 63 Punkte hat, aber nicht im oberen Spiel
        testTable.table["Vierer"] = 12
        testTable.table["FullHouse"] = 25
        testTable.table["Fünfer"] = 15
        testTable.table["Viererpasch"] = 24
        testTable.table["Sechser"] = 18
        testTable.table["Dreierpasch"] = 18
        self.assertTrue(testTable.checkBonus())     #überprüfe, dass der Bonus jetzt tatsächlich angerechnet wird


if __name__ == '__main__':
    unittest.main()