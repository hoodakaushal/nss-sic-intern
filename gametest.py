__author__ = 'hooda'
import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import speech
import ui_playWindow


class PlayWindow(QMainWindow, ui_playWindow.Ui_PlayWindow):
    def __init__(self, parent=None):
        super(PlayWindow, self).__init__(parent)
        self.setupUi(self)
        self.resultLabel.clear()
        self.makewords('data\\words\\easy')
        self.resetWord()

        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.checker)
        self.connect(self.checkButton, SIGNAL('clicked()'), self.checker)

    def checker(self):
        speech.say("Checking...")
        scrambled = self.scrambledLabel.text()
        cand = self.lineEdit.text()
        validPerm = sorted(scrambled) == sorted(cand)
        validWord = self.isWord(cand)
        if validPerm and validWord:
            self.resultLabel.setText("Correct!")
            speech.say("Correct")
            self.resetWord()
            self.lineEdit.clear()
        else:
            self.resultLabel.setText("Wrong! Right answer is " + self.answer)
            speech.say("Wrong! Right answer is " + self.answer)

    def resetWord(self):
        newWord = random.choice(tuple(self.words))
        self.answer = newWord
        newWord = self.scrambleWord(newWord)
        self.scrambledLabel.setText(newWord)

    def scrambleWord(self, qstring):
        s = str(qstring)
        l = list(s)
        random.shuffle(l)
        s = ''.join(l)
        q = QString(s)
        if q == qstring:
            return self.scrambleWord(qstring)
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
    # playWindow.scrambledLabel.setText("itioncompet")
    # print('competition' in playWindow.words)
    playWindow.show()
    app.exec_()


main()