#Authors: James King, Sven Krueger
#22.09.21

import sys
from PyQt5 import uic, QtWidgets, QtCore

from kniffel_gui import Player

Ui_MainWindow, WindowBaseClass = uic.loadUiType("main_window.ui")
class MyDialog(WindowBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.startedGame = False    #Attribut, das angibt, ob das Spiel schon gestartet ist oder noch Namen eingetragen werden

    def acceptPlayerName(self):
    #Hier werden die Spieler erstellt
        if not self.startedGame or self.widget._logic.numberOfPlayers == 0:    #neue Spieler können nur hinzugefügt werden, wenn das Spiel noch nicht gestartet ist
            #erstelle einen Spieler mit dem Namen, der im Textfeld eingegeben wurde und füge ihn der Liste aller Spieler hinzu
            name = self.textEdit_PlayerName.toPlainText()
            self.widget._logic.players.append(Player(name))
            self.widget._logic.numberOfPlayers = len(self.widget._logic.players)
            
            player1 = self.widget._logic.players[0]
            self.widget._logic.playingPlayer = player1  #setze den ersten Spieler als playingPlayer
            self.widget._logic.playerRollCounter = 0

            #zeige die erzielten Punkte des aktuellen Spielers
            textRegistered = "erzielte Punkte:\n"
            for figur in player1.registered.table:
                textRegistered += figur + ": " + str(player1.registered.table[figur]) + "\n"

            #zeige den Gesamtscore aller Spieler
            textScore = "Gesamtscore:\n"
            for player in self.widget._logic.players:
                textScore += player.name + ": " + str(player.sumOfAllPoints) + "\n"
            
            #aktualisiere die Textfelder
            self.widget.showPlayerName.emit(player1.name)
            self.widget.showRoundCounter.emit("1")
            self.widget.showRegistered.emit(textRegistered)
            self.widget.showScore.emit(textScore)
            self.widget.showRollCounter.emit("0")
    
    def startGame(self):
    #das Spiel startet, wenn gewürfelt wird
        self.startedGame = True

    def wuerfeln(self):
    #wird ausgeführt, wenn man auf "Würfeln" klickt
        #erstelle eine Liste von Indizes der Würfel, die nochmal geworfen werden sollen
        chosen = []
        if not self.checkBoxWuerfel1.isChecked():
            chosen.append(0)
        if not self.checkBoxWuerfel2.isChecked():
            chosen.append(1)
        if not self.checkBoxWuerfel3.isChecked():
            chosen.append(2)
        if not self.checkBoxWuerfel4.isChecked():
            chosen.append(3)
        if not self.checkBoxWuerfel5.isChecked():
            chosen.append(4)

        if self.widget._logic.playerRollCounter == 0:   #wenn man das erste Mal würfelt, kann man noch keine Würfel behalten
            self.widget.wuerfeln([0, 1, 2, 3, 4])
        else:
            self.widget.wuerfeln(chosen)
    
    #folgende Methoden übergeben den Zustand der checkBoxes an das Widget und lassen es neu zeichnen, sobald eine checkBox angeklickt wird
    def checkCheckBox1(self):
        self.widget.checkBox1 = self.checkBoxWuerfel1.isChecked()
        self.widget.update()

    def checkCheckBox2(self):
        self.widget.checkBox2 = self.checkBoxWuerfel2.isChecked()
        self.widget.update()

    def checkCheckBox3(self):
        self.widget.checkBox3 = self.checkBoxWuerfel3.isChecked()
        self.widget.update()

    def checkCheckBox4(self):
        self.widget.checkBox4 = self.checkBoxWuerfel4.isChecked()
        self.widget.update()

    def checkCheckBox5(self):
        self.widget.checkBox5 = self.checkBoxWuerfel5.isChecked()
        self.widget.update()

    #folgende Funktionen übergeben an das Widget, was der aktuelle Spieler eintragen will, sobald der Spieler den entsprechenden Button klickt und bereiten alles für den nächsten Spieler vor
    def registerEinser(self):
        self.widget.register("Einser")
        self.reset()

    def registerZweier(self):
        self.widget.register("Zweier")
        self.reset()

    def registerDreier(self):
        self.widget.register("Dreier")
        self.reset()

    def registerVierer(self):
        self.widget.register("Vierer")
        self.reset()

    def registerFuenfer(self):
        self.widget.register("Fünfer")
        self.reset()

    def registerSechser(self):
        self.widget.register("Sechser")
        self.reset()

    def registerDreierpasch(self):
        self.widget.register("Dreierpasch")
        self.reset()

    def registerViererpasch(self):
        self.widget.register("Viererpasch")
        self.reset()

    def registerFullHouse(self):
        self.widget.register("FullHouse")
        self.reset()

    def registerKleineStrasse(self):
        self.widget.register("KleineStrasse")
        self.reset()

    def registerGrosseStrasse(self):
        self.widget.register("GrosseStrasse")
        self.reset()

    def registerKniffel(self):
        self.widget.register("Kniffel")
        self.reset()

    def registerChance(self):
        self.widget.register("Chance")
        self.reset()
        
    def reset(self):
    #Hier werden die checkBoxes auf "Nicht ausgewählt" gesetzt
        self.checkBoxWuerfel1.setChecked(False)
        self.widget.checkBox1 = False
        self.checkBoxWuerfel2.setChecked(False)
        self.widget.checkBox2 = False
        self.checkBoxWuerfel3.setChecked(False)
        self.widget.checkBox3 = False
        self.checkBoxWuerfel4.setChecked(False)
        self.widget.checkBox4 = False
        self.checkBoxWuerfel5.setChecked(False)
        self.widget.checkBox5 = False
        self.widget.update()

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(application.exec_())