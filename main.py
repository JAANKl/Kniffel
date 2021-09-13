import sys
from PyQt5 import uic, QtWidgets, QtCore

Ui_MainWindow, WindowBaseClass = uic.loadUiType("main_window.ui")
class MyDialog(WindowBaseClass, Ui_MainWindow):
    chosenDice = QtCore.pyqtSignal(str) # die Würfel die man behalten will (Übergabe an Label)

    def __init__(self, parent=None):
        WindowBaseClass.__init__(self, parent)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

    def checkChosenDice(self):
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
        #self.widget._logic.rollDice(chosen, self.widget._logic.playerRollCounter)
        #self.widget._logic.playerRollCounter += 1
        print(chosen)
        chosen = ",".join([str(zahl) for zahl in chosen])
        self.chosenDice.emit(chosen)


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(application.exec_())
