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
        if self.checkBoxWuerfel1.isChecked():
            chosen.append(1)
        if self.checkBoxWuerfel2.isChecked():
            chosen.append(2)
        if self.checkBoxWuerfel3.isChecked():
            chosen.append(3)
        if self.checkBoxWuerfel4.isChecked():
            chosen.append(4)
        if self.checkBoxWuerfel5.isChecked():
            chosen.append(5)
        print(chosen)
        chosen = ",".join([str(zahl) for zahl in chosen])
        self.chosenDice.emit(chosen)


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(application.exec_())
