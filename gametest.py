__author__ = 'hooda'
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_playWindow


class PlayWindow(QMainWindow, ui_playWindow.Ui_PlayWindow):
    def __init__(self, parent=None):
        super(PlayWindow, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.checker)


    def checker(self):
        scrambled = self.scrambledLabel.text()
        cand = self.lineEdit.text()
        valid = sorted(scrambled) == sorted(cand)
        if valid:
            self.resultLabel.setText("Correct!")
        else:
            self.resultLabel.setText("Wrong!")


def tester(scrambled, cand):
    if cand == scrambled:
        return True
    else:
        return False


def main():
    app = QApplication(sys.argv)
    playWindow = PlayWindow()
    playWindow.scrambledLabel.setText("onpyth")
    playWindow.show()
    app.exec_()


main()