import os

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import Qt
from PyQt5 import QtCore

from kniffel_gui import AlreadyRegistered, Game, TooManyRolls

class WuerfelWidget(QWidget):
    #verschiedene Signale für verschiedene Anzeigen
    showPossibilities = QtCore.pyqtSignal(str)
    showRegistered = QtCore.pyqtSignal(str)
    showPlayerName = QtCore.pyqtSignal(str)
    showRoundCounter = QtCore.pyqtSignal(str)
    showRollCounter = QtCore.pyqtSignal(str)
    showStatus = QtCore.pyqtSignal(str)
    showScore = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        #Attribute, die angeben, ob die entsprechende checkBox ausgewählt ist
        self.checkBox1 = False
        self.checkBox2 = False
        self.checkBox3 = False
        self.checkBox4 = False
        self.checkBox5 = False
        self.chosen = []    #Liste für die ausgewählten Würfel

        #Größe der Würfelbilder
        self.dice_size = 50
        self.dice_spacing = 8

        #Größe des Widgets
        self.setFixedWidth(self.dice_spacing + 5 * (self.dice_size + self.dice_spacing))
        self.setFixedHeight(2 * self.dice_spacing + self.dice_size)

        #Bilder für die normalen Würfel
        dice1 = QPixmap(os.path.join("dice", "dice1.png"))
        dice2 = QPixmap(os.path.join("dice", "dice2.png"))
        dice3 = QPixmap(os.path.join("dice", "dice3.png"))
        dice4 = QPixmap(os.path.join("dice", "dice4.png"))
        dice5 = QPixmap(os.path.join("dice", "dice5.png"))
        dice6 = QPixmap(os.path.join("dice", "dice6.png"))

        #Bilder für die ausgewählten Würfel
        dice1_highlighted = QPixmap(os.path.join("dice_highlighted", "dice1_highlighted.png"))
        dice2_highlighted = QPixmap(os.path.join("dice_highlighted", "dice2_highlighted.png"))
        dice3_highlighted = QPixmap(os.path.join("dice_highlighted", "dice3_highlighted.png"))
        dice4_highlighted = QPixmap(os.path.join("dice_highlighted", "dice4_highlighted.png"))
        dice5_highlighted = QPixmap(os.path.join("dice_highlighted", "dice5_highlighted.png"))
        dice6_highlighted = QPixmap(os.path.join("dice_highlighted", "dice6_highlighted.png"))

        #enthält die Bilder der normalen Würfel
        self._diceImageMap = {1: dice1.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              2: dice2.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              3: dice3.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              4: dice4.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              5: dice5.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                              6: dice6.scaledToWidth(self.dice_size, Qt.SmoothTransformation)}
        
        #enthält die Bilder der ausgewählten Würfel
        self._diceImageMap_highlighted = {1: dice1_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                                          2: dice2_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                                          3: dice3_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                                          4: dice4_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                                          5: dice5_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation),
                                          6: dice6_highlighted.scaledToWidth(self.dice_size, Qt.SmoothTransformation)}

        self._logic = Game()    #referenziere die Spiellogik

    def wuerfeln(self, chosenIndices):
    #Hier werden die gewünschten Würfel nochmal geworfen
        try:
            self._logic.rollDice(chosenIndices, self._logic.playerRollCounter)
            self._logic.playerRollCounter += 1
            self.showRollCounter.emit(str(self._logic.playerRollCounter))

            possibilities = self._logic.possibilities()
            textPossibilities = "Möglichkeiten:\n"

            for name in self._logic.playingPlayer.registered.table:
                if self._logic.playingPlayer.registered.table[name] is None:
                    textPossibilities += name + ": " + str(possibilities.table[name]) + "\n"

            self.showPossibilities.emit(textPossibilities)  #zeige dem Spieler die Möglichkeiten zum Eintragen an
            self.showStatus.emit("")
            self.update()

        except TooManyRolls as tmr:
            self.showStatus.emit(str(tmr))

        except AttributeError:
            self.showStatus.emit("Bitte Namen eingeben")
            #Hier müsste startedGame eigentlich wieder auf False gesetzt werden, aber man hat keinen Zugriff drauf :(

    def register(self, figur):
    #Hier wird die gewünschte Kategorie eingetragen
        try:
            self._logic.register(figur)

            #Bonusabfrage
            if self._logic.playingPlayer.registered.checkBonus() and not self._logic.playingPlayer.bonusAchieved:
                self._logic.playingPlayer.bonusAchieved = True
                self.showStatus.emit("Sie haben den Bonus erreicht")
                self._logic.playingPlayer.registered.table["Bonus"] = 35
                self._logic.playingPlayer.sumOfAllPoints += 35

            self._logic.playerRollCounter = 0   #für den nächsten Spieler den Zähler wieder auf 0 setzen
            self._logic.playingPlayer.sumOfAllPoints += self._logic.playingPlayer.registered.table[figur]   #aktualisiert die Gesamtpunktzahl

            playerIndex = self._logic.players.index(self._logic.playingPlayer)
            #nächster Spieler wird neuer playingPlayer
            if playerIndex == self._logic.numberOfPlayers - 1:
                self._logic.playingPlayer = self._logic.players[0]
                self._logic.roundCounter += 1   #wenn, wieder der erste Spieler an der Reihe ist, startet die nächste Runde
            else:
                self._logic.playingPlayer = self._logic.players[playerIndex + 1]
                
            #bereits erzielte Punkte des spielenden Spielers
            textRegistered = "erzielte Punkte:\n"
            for name in self._logic.playingPlayer.registered.table:
                textRegistered += name + ": " + str(self._logic.playingPlayer.registered.table[name]) + "\n"
            
            #Gesamtpunktzahlen aller Spieler
            textScore = "Gesamtscore:\n"
            for player in self._logic.players:
                textScore += player.name + ": " + str(player.sumOfAllPoints) + "\n"

            #alle Textfelder aktualisieren
            self.showPlayerName.emit(self._logic.playingPlayer.name)
            self.showRoundCounter.emit(str(self._logic.roundCounter))
            self.showRollCounter.emit("0")
            self.showRegistered.emit(textRegistered)
            self.showPossibilities.emit("Möglichkeiten:\n")
            self.showScore.emit(textScore)
            
        except AlreadyRegistered as ar:
            self.showStatus.emit(str(ar))

    def paintEvent(self, event):
    #Hier wird das Widget gezeichnet
        painter = QPainter(self)

        #Hintergrund zeichnen
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(event.rect())

        x = self.dice_spacing
        y = self.dice_spacing

        self.chosen = [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4, self.checkBox5]  #Liste der ausgewählten Würfel

        for i in range(5):
            #je nach dem, ob der Würfel ausgewählt ist oder nicht, soll ein entsprechender Würfel gezeichnet werden
            if self.chosen[i]:
                painter.drawPixmap(x, y, self._diceImageMap_highlighted[self._logic.dice.roll[i]])
            else:
                painter.drawPixmap(x, y, self._diceImageMap[self._logic.dice.roll[i]])
            x += self.dice_size + self.dice_spacing
