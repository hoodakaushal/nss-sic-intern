__author__ = 'hooda'
import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_playWindow


class PlayWindow(QMainWindow, ui_playWindow.Ui_PlayWindow):
    def __init__(self, parent=None):
        super(PlayWindow, self).__init__(parent)
        self.setupUi(self)
        self.resultLabel.clear()
        self.makewords('words')

        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.checker)
        self.connect(self.checkButton, SIGNAL('clicked()'), self.checker)


    def checker(self):
        scrambled = self.scrambledLabel.text()
        cand = self.lineEdit.text()
        validPerm = sorted(scrambled) == sorted(cand)
        validWord = self.isWord(cand)
        if validPerm and validWord:
            self.resultLabel.setText("Correct!")
            self.resetWord()
            self.lineEdit.clear()
        else:
            self.resultLabel.setText("Wrong!")


    def resetWord(self):
        newWord = random.choice(tuple(self.words))
        newWord = self.scrambleWord(newWord)
        self.scrambledLabel.setText(newWord)

    def scrambleWord(self, qstring):
        s = str(qstring)
        l = list(s)
        random.shuffle(l)
        s = ''.join(l)
        return QString(s)

    def makewords(self, wordfile):
        wordfile = open(wordfile)
        wordset = set()
        for line in wordfile:
            wordset.add(QString(line.rstrip()))
        self.words = wordset

    def isWord(self, cand):
        """

        :rtype : bool
        """
        if cand in self.words:
            print('found', cand)
            return True
        else:
            print('not found', cand)
            return False


def main():
    app = QApplication(sys.argv)
    playWindow = PlayWindow()
    playWindow.scrambledLabel.setText("itioncompet")
    # print('competition' in playWindow.words)
    playWindow.show()
    app.exec_()


main()