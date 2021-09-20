import unittest
import kniffel_konsole as _logic

class TestKniffel(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
