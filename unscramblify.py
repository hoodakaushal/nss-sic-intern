__author__ = 'hooda'

__author__ = 'hooda'
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import speech
import ui_startWindow


class StartWindow(QMainWindow, ui_startWindow.Ui_startWindow):
    def __init__(self, parent=None):
        super(StartWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setupUi(self)
        # self.setCentralWidget(self.verticalLayout)


        qApp.focusChanged.connect(self.handleFocusChange)
        # self.connect(self.newButton, SIGNAL('tabSignal()'), lambda t="New Game.": speakNewButton(t))
        # self.connect(self.profileButton, SIGNAL('tabSignal()'), lambda t="Change Profile.": speakNewButton(t))
        # self.connect(self.wordsetButton, SIGNAL('tabSignal()'), lambda t="Select Wordset.": speakNewButton(t))
        # self.connect(self.difficultyButton, SIGNAL('tabSignal()'), lambda t="Select Difficulty.": speakNewButton(t))
        # self.connect(self.highscoresButton, SIGNAL('tabSignal()'), lambda t="Highscores.": speakNewButton(t))
        # self.connect(self.helpButton, SIGNAL('tabSignal()'), lambda t="Help.": speakNewButton(t))
        # self.connect(self.exitButton, SIGNAL('tabSignal()'), lambda t="Exit.": speakNewButton(t))

    def handleFocusChange(self, old, new):
        if isinstance(new, QPushButton):
            speech.say(new.text() + ' .')
            # speech.say('1 2 3 4.')


class FocusButton(QPushButton):
    def __init__(self, parent=None):
        super(FocusButton, self).__init__(parent)

    tabSignal = pyqtSignal()

    def focusInEvent(self, QFocusEvent):
        self.emit(SIGNAL('tabSignal()'))


def speakTestButton(widget1, widget2):
    speech.say("Fuck this shit!")


def speakNewButton(t):
    print("LOL")
    speech.say(t)

    # class FocusButton(QPushButton):
    # def __init__(self, parent=None):
    #         super(FocusButton, self).__init__(parent)
    #
    #     tabSignal = pyqtSignal()

    def focusInEvent(self, QFocusEvent):
        self.emit(SIGNAL('tabSignal()'))


def main():
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    # playWindow.scrambledLabel.setText("itioncompet")
    # print('competition' in playWindow.words)
    # assert isinstance(startWindow.newButton, ui_startWindow.FocusButton)
    startWindow.show()
    app.exec_()


main()