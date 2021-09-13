import sys
from PyQt5 import uic, QtWidgets, QtCore

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
            self.widget._logic.playerNames.append(name)
            self.widget._logic.numberOfPlayers = len(self.widget._logic.playerNames)
            print(self.widget._logic.playerNames)
    
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
    
    def registerEinser(self):
        self.widget.register("Einser")

    def registerZweier(self):
        self.widget.register("Zweier")

    def registerDreier(self):
        self.widget.register("Dreier")

    def registerVierer(self):
        self.widget.register("Vierer")

    def registerFuenfer(self):
        self.widget.register("Fünfer")

    def registerSechser(self):
        self.widget.register("Sechser")

    def registerDreierpasch(self):
        self.widget.register("Dreierpasch")

    def registerViererpasch(self):
        self.widget.register("Viererpasch")

    def registerFullHouse(self):
        self.widget.register("FullHouse")

    def registerKleineStrasse(self):
        self.widget.register("KleineStrasse")

    def registerGrosseStrasse(self):
        self.widget.register("GrosseStrasse")

    def registerKniffel(self):
        self.widget.register("Kniffel")
    
    def registerChance(self):
        self.widget.register("Chance")


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(application.exec_())
