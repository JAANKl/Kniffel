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
    showStatus = QtCore.pyqtSignal(str)
    showScore = QtCore.pyqtSignal(str)


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

    def wuerfeln(self, chosenIndices):
        try:
            self._logic.rollDice(chosenIndices, self._logic.playerRollCounter)
            self._logic.playerRollCounter += 1
            self.showRollCounter.emit(str(self._logic.playerRollCounter))

            possibilities = self._logic.possibilities()
            textPossibilities = "Möglichkeiten:\n"

            for name in self._logic.playingPlayer.registered.table:
                if self._logic.playingPlayer.registered.table[name] is None:
                    textPossibilities += name + ": " + str(possibilities.table[name]) + "\n"

            self.showPossibilities.emit(textPossibilities)
            self.showStatus.emit("")
            self.update()

        except TooManyRolls as tmr:
            self.showStatus.emit(str(tmr))

    def register(self, figur):
        try:
            self._logic.register(figur)

            #Bonusabfrage
            if self._logic.playingPlayer.registered.checkBonus() and not self._logic.playingPlayer.bonusAchieved:
                self._logic.playingPlayer.bonusAchieved = True
                self.showStatus.emit("Sie haben den Bonus erreicht")
                self._logic.playingPlayer.registered.table["Bonus"] = 35
                self._logic.playingPlayer.sumOfAllPoints += 35

            self._logic.playerRollCounter = 0
            self._logic.playingPlayer.sumOfAllPoints += self._logic.playingPlayer.registered.table[figur]
            #text += "Gesamtpunktzahl: " + str(self._logic.player.sumOfAllPoints)
            playerIndex = self._logic.players.index(self._logic.playingPlayer)
            if playerIndex == self._logic.numberOfPlayers - 1:
                self._logic.playingPlayer = self._logic.players[0]
                self._logic.roundCounter += 1
            else:
                self._logic.playingPlayer = self._logic.players[playerIndex + 1]
                

            textRegistered = "erzielte Punkte:\n"
            for name in self._logic.playingPlayer.registered.table:
                textRegistered += name + ": " + str(self._logic.playingPlayer.registered.table[name]) + "\n"
            
            textScore = "Gesamtscore:\n"
            for player in self._logic.players:
                textScore += player.name + ": " + str(player.sumOfAllPoints) + "\n"

            self.showPlayerName.emit(self._logic.playingPlayer.name)
            self.showRoundCounter.emit(str(self._logic.roundCounter))
            self.showRollCounter.emit("0")
            self.showRegistered.emit(textRegistered)
            self.showPossibilities.emit("Möglichkeiten:\n")
            self.showScore.emit(textScore)
            
        except AlreadyRegistered as ar:
            self.showStatus.emit(str(ar))

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
