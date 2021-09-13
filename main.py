import sys
from PyQt5 import uic, QtWidgets, QtCore

from kniffel_gui import Player

Ui_MainWindow, WindowBaseClass = uic.loadUiType("main_window.ui")
class MyDialog(WindowBaseClass, Ui_MainWindow):

    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.startedGame = False

    def acceptPlayerName(self):
        if not self.startedGame:
            name = self.textEdit_PlayerName.toPlainText()
            self.widget._logic.players.append(Player(name))
            self.widget._logic.numberOfPlayers = len(self.widget._logic.players)
            
            player1 = self.widget._logic.players[0]
            self.widget._logic.playingPlayer = player1
            textRegistered = "erzielte Punkte:\n"
            for figur in player1.registered.table:
                textRegistered += figur + ": " + str(player1.registered.table[figur]) + "\n"

            textScore = "Gesamtscore:\n"
            for player in self.widget._logic.players:
                textScore += player.name + ": " + str(player.sumOfAllPoints) + "\n"
            
            self.widget.showPlayerName.emit(player1.name)
            self.widget.showRoundCounter.emit("1")
            self.widget.showRegistered.emit(textRegistered)
            self.widget.showScore.emit(textScore)
    
    def startGame(self):
        self.startedGame = True

    def wuerfeln(self):
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

        if self.widget._logic.playerRollCounter == 0:
            self.widget.wuerfeln([0, 1, 2, 3, 4])
        else:
            self.widget.wuerfeln(chosen)
    
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
