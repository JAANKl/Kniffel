import unittest
import kniffel_konsole as _logic

class TestKniffel(unittest.TestCase):

    def test_Numbers(self):
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
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkDreierpasch()[0])
        self.assertEqual(testDice.checkDreierpasch()[1], 28)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkDreierpasch()[0])
        self.assertEqual(testDice.checkDreierpasch()[1], 0)
    
    def test_checkViererpasch(self):
        testDice = _logic.Dice([6, 6, 6, 6, 5])
        self.assertTrue(testDice.checkViererpasch()[0])
        self.assertEqual(testDice.checkViererpasch()[1], 29)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkViererpasch()[0])
        self.assertEqual(testDice.checkViererpasch()[1], 0)

    def test_checkFullHouse(self):
        testDice = _logic.Dice([6, 6, 6, 5, 5])
        self.assertTrue(testDice.checkFullHouse()[0])
        self.assertEqual(testDice.checkFullHouse()[1], 25)

        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertFalse(testDice.checkFullHouse()[0])
        self.assertEqual(testDice.checkFullHouse()[1], 0)
    
    def test_checkKleineStrasse(self):
        testDice = _logic.Dice([1, 2, 3, 4, 2])
        self.assertTrue(testDice.checkKleineStrasse()[0])
        self.assertEqual(testDice.checkKleineStrasse()[1], 30)

        testDice = _logic.Dice([1, 2, 3, 5, 6])
        self.assertFalse(testDice.checkKleineStrasse()[0])
        self.assertEqual(testDice.checkKleineStrasse()[1], 0)
    
    def test_checkGrosseStrasse(self):
        testDice = _logic.Dice([1, 2, 3, 4, 5])
        self.assertTrue(testDice.checkGrosseStrasse()[0])
        self.assertEqual(testDice.checkGrosseStrasse()[1], 40)

        testDice = _logic.Dice([1, 2, 3, 5, 6])
        self.assertFalse(testDice.checkGrosseStrasse()[0])
        self.assertEqual(testDice.checkGrosseStrasse()[1], 0)
    
    def test_checkKniffel(self):
        testDice = _logic.Dice([1, 1, 1, 1, 1])
        self.assertTrue(testDice.checkKniffel()[0])
        self.assertEqual(testDice.checkKniffel()[1], 50)

        testDice = _logic.Dice([1, 1, 1, 1, 2])
        self.assertFalse(testDice.checkKniffel()[0])
        self.assertEqual(testDice.checkKniffel()[1], 0)
    
    def test_checkChance(self):
        testDice = _logic.Dice([1, 3, 4, 5, 5])
        self.assertTrue(testDice.checkChance()[0])
        self.assertEqual(testDice.checkChance()[1], 18)

        testDice = _logic.Dice([3, 3, 3, 3, 3])
        self.assertTrue(testDice.checkChance()[0])
        self.assertEqual(testDice.checkChance()[1], 15)
    
    def test_register(self):
        testPlayer = _logic.Player("Test")
        testPlayer.register("GrosseStrasse", 40)
        self.assertEqual(testPlayer.registered.table["GrosseStrasse"], 40)
        self.assertIsNone(testPlayer.registered.table["Kniffel"])
        self.assertEqual(testPlayer.sumOfAllPoints, 40)

        testPlayer.register("Sechser", 18)
        self.assertEqual(testPlayer.registered.table["Sechser"], 18)
        self.assertIsNone(testPlayer.registered.table["Zweier"])
        self.assertEqual(testPlayer.sumOfAllPoints, 58)
    
    def test_checkBonus(self):
        testTable = _logic.Table()
        testTable.table["Chance"] = 23
        testTable.table["Einser"] = 3
        testTable.table["Kniffel"] = 50
        testTable.table["Zweier"] = 6
        testTable.table["GrosseStrasse"] = 40
        testTable.table["Dreier"] = 9
        testTable.table["KleineStrasse"] = 30
        self.assertFalse(testTable.checkBonus())
        testTable.table["Vierer"] = 12
        testTable.table["FullHouse"] = 25
        testTable.table["Fünfer"] = 15
        testTable.table["Viererpasch"] = 24
        testTable.table["Sechser"] = 18
        testTable.table["Dreierpasch"] = 18
        self.assertTrue(testTable.checkBonus())


if __name__ == '__main__':
    unittest.main()
