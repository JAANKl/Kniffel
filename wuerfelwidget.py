import os

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt

from kniffel_gui import Game

class WuerfelWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.dice_size = 50
        self.dice_spacing = 8

        self.setFixedWidth(self.dice_spacing + 5 * (self.dice_size + self.dice_spacing))

        dice1 = QPixmap(os.path.join("dice", "dice1.png"))
        dice2 = QPixmap(os.path.join("dice", "dice2.png"))
        dice3 = QPixmap(os.path.join("dice", "dice3.png"))
        dice4 = QPixmap(os.path.join("dice", "dice4.png"))
        dice5 = QPixmap(os.path.join("dice", "dice5.png"))
        dice6 = QPixmap(os.path.join("dice", "dice6.png"))

        self._diceImageMap = {1: dice1.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              2: dice2.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              3: dice3.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              4: dice4.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              5: dice5.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              6: dice6.scaledToWidth(self.dice_size, Qt.SmoothTransformation)}

        self._logic = Game()

    def wuerfeln(self):
        self._logic.rollDice([0, 1, 2, 3, 4])
        self.update()

    def eintragen(self, name):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)

        #draw background
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGreen)
        painter.drawRect(event.rect())

        x = self.dice_spacing
        y = self.dice_spacing
        for i in range(5):
            painter.drawPixmap(x, y, self._diceImageMap[self._logic.dice.roll[i]])
            x += self.dice_size + self.dice_spacing
