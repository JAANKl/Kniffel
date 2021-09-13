import os

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt
from PyQt5 import QtCore

from kniffel_gui import AlreadyRegistered, Game, TooManyRolls

class WuerfelWidget(QWidget):

    showPossibilities = QtCore.pyqtSignal(str)
    showRegistered = QtCore.pyqtSignal(str)
    showPlayerName = QtCore.pyqtSignal(str)
    showRoundCounter = QtCore.pyqtSignal(str)
    showRollCounter = QtCore.pyqtSignal(str)
    showError = QtCore.pyqtSignal(str)


    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.dice_size = 50
        self.dice_spacing = 8

        self.setFixedWidth(self.dice_spacing + 5 * (self.dice_size + self.dice_spacing))
        self.setFixedHeight(2 * self.dice_spacing + self.dice_size)

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
        try:
            self._logic.rollDice([0, 1, 2, 3, 4], self._logic.playerRollCounter)
            self._logic.playerRollCounter += 1
            self.showPlayerName.emit(self._logic.player.name)
            self.showRoundCounter.emit(str(self._logic.roundCounter))
            self.showRollCounter.emit(str(self._logic.playerRollCounter))

            possibilities = self._logic.possibilities()
            text = ""
            for name in possibilities.table:
                if self._logic.player.registered.table[name] is None:
                    text += name + ": " + str(possibilities.table[name]) + "\n"
            self.showPossibilities.emit(text)
            self.update()
        except TooManyRolls as tmr:
            self.showError.emit(str(tmr))

    def registerEinser(self):
        try:
            self._logic.register("Einser")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))
    
    def registerZweier(self):
        try:
            self._logic.register("Zweier")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerDreier(self):
        try:
            self._logic.register("Dreier")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerVierer(self):
        try:
            self._logic.register("Vierer")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerFuenfer(self):
        try:
            self._logic.register("Fünfer")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerSechser(self):
        try:
            self._logic.register("Sechser")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerDreierpasch(self):
        try:
            self._logic.register("Dreierpasch")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerViererpasch(self):
        try:
            self._logic.register("Viererpasch")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerFullHouse(self):
        try:
            self._logic.register("FullHouse")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerKleineStrasse(self):
        try:
            self._logic.register("KleineStrasse")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerGrosseStrasse(self):
        try:
            self._logic.register("GrosseStrasse")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerKniffel(self):
        try:
            self._logic.register("Kniffel")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def registerChance(self):
        try:
            self._logic.register("Chance")
            text = ""
            for figur in self._logic.player.registered.table:
                text += figur + ": " + str(self._logic.player.registered.table[figur]) + "\n"
            self.showRegistered.emit(text)
            self._logic.playerRollCounter = 0
            self._logic.roundCounter += 1
        except AlreadyRegistered as ar:
            self.showError.emit(str(ar))

    def possibilities(self):
        pass

    def paintEvent(self, event):
        painter = QPainter(self)

        #draw background
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(event.rect())

        x = self.dice_spacing
        y = self.dice_spacing
        for i in range(5):
            painter.drawPixmap(x, y, self._diceImageMap[self._logic.dice.roll[i]])
            x += self.dice_size + self.dice_spacing
