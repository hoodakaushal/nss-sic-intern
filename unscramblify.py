import random

__author__ = 'hooda'

import sys
import os
from collections import OrderedDict

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import speech
import ui_difficultyDialog
import ui_helpWindow
import ui_highscoresDialog
import ui_playWindow
import ui_profileDialog
import ui_newProfileDialog
import ui_selectProfileDialog
import ui_startWindow





# The first window that opens. Not much to it, just used to get to the various functions.
# TODO : First-start help message.
# TODO : Should help exist as its own window, or a context dependant popup.
class StartWindow(QMainWindow, ui_startWindow.Ui_startWindow):
    def __init__(self, parent=None):
        """
        Initialise the start window.
        Read data from the data folder - profiles, highscores etc.
        Setup the appropriate SIGNAL/SLOT connections.

        :param parent:Parent of this window. Defaults to None since it is a main window.
        """
        super(StartWindow, self).__init__(parent)
        self.playWindow = None
        self.setupUi(self)
        self.readData()
        # Speak the name of the button which has focus. Not perfect - clicking a button, or alt-tabbing around also triggers.
        qApp.focusChanged.connect(self.handleFocusChange)

        # Connections for the buttons. Self explanatory.
        self.newButton.clicked.connect(self.createPlayWindow)
        self.newTimedButton.clicked.connect(self.createTimedPlayWindow)
        self.profileButton.clicked.connect(self.changeProfile)
        self.difficultyButton.clicked.connect(self.changeDifficulty)
        self.highscoresButton.clicked.connect(self.showHighscores)
        self.helpButton.clicked.connect(self.showHelp)
        self.exitButton.clicked.connect(self.saveAndExit)

    def createPlayWindow(self):
        self.playWindow = PlayWindow(self.profile, False, self)
        self.hide()
        self.playWindow.show()

    def createTimedPlayWindow(self):
        self.playWindow = PlayWindow(self.profile, True, self)
        self.hide()
        self.playWindow.show()

    def changeProfile(self):
        # print self.profile.name
        profileDialog = ProfileDialog(self)
        if profileDialog.exec_():
            if profileDialog.new:
                newProfile = Profile(profileDialog.profile, 'easy', 0, 0, set())
                f = open('data\\profiles\\' + str(profileDialog.profile), 'w')
                f.write('easy' + '\n')
                f.write('0' + '\n')
                f.write('0' + '\n')
                f.write('\n')
                f.close()
                self.profile = newProfile
            else:
                self.loadProfile(str(profileDialog.profile))

    def changeDifficulty(self):
        difficultyDialog = DifficultyDialog(self)
        difficultyDialog.exec_()
        if difficultyDialog.difficulty != '':
            self.profile.difficulty = difficultyDialog.difficulty

    def showHighscores(self):
        highscoresDialog = HighscoresDialog(self)
        highscoresDialog.exec_()

    def showHelp(self):
        self.helpWindow = HelpWindow(self)
        self.hide()
        self.helpWindow.show()

    def readData(self):
        f = open('data//lastprofile')
        lastProfile = f.readline().rstrip()
        self.loadProfile(lastProfile, 0)

        f = open('data\\highscores.txt')
        lines = f.readlines()
        scores = OrderedDict()
        # print(lines)
        i = 0
        while i < (len(lines)):
            profile = lines[i].rstrip()
            infiScore = int(lines[i + 1].rstrip())
            timeScore = int(lines[i + 2].rstrip())
            i = i + 4
            scores[profile] = (infiScore, timeScore)
        self.highscores = scores
        f.close()


    def loadProfile(self, profile, code=1):
        if code == 1:
            self.saveProfile()
        name = profile
        f = open('data\\profiles\\' + name)
        difficulty = f.readline().rstrip()
        infiScore = str(f.readline().rstrip())
        timeScore = str(f.readline().rstrip())
        f.readline()
        blacklist = set()
        for line in f.readlines():
            blacklist.add(QString(line.rstrip()))
        self.profile = Profile(name, difficulty, infiScore, timeScore, blacklist)

    def saveProfile(self):
        f = open('data\\profiles\\' + self.profile.name, 'w')
        f.write(self.profile.difficulty + '\n')
        f.write(str(self.profile.infiScore) + '\n')
        f.write(str(self.profile.timeScore) + '\n')
        f.write('\n')
        for word in self.profile.blaclist:
            f.write(str(word) + '\n')
        f.close()


    def handleFocusChange(self, old, new):
        if isinstance(new, QPushButton):
            speech.say(new.text().replace("&", '') + '.')
            # print self.currentProfile
            # speech.say('1 2 3 4.')

    def saveAndExit(self):
        self.saveProfile()
        self.writeHighscore()
        f = open('data\\lastprofile', 'w')
        f.write(self.profile.name)
        f.close()
        QCoreApplication.instance().exit()

    def writeHighscore(self):
        f = open('data\\highscores.txt')
        lines = f.readlines()
        scores = []
        # print(lines)
        i = 0
        while i < (len(lines)):
            profile = lines[i].rstrip()
            infiScore = int(lines[i + 1].rstrip())
            timeScore = int(lines[i + 2].rstrip())
            i = i + 4
            scores += [(profile, infiScore, timeScore)]
        scores += [(self.profile.name, self.profile.infiScore, self.profile.timeScore)]

        def getTimeHS(x):
            return x[2]

        scores = sorted(scores, key=getTimeHS)
        scores = scores[0:10]
        f = open('data\\highscores.txt', 'w')
        for item in scores:
            f.write('%s\n%i\n%i\n\n' % (item[0], int(item[1]), int(item[2])))
        f.close()

    def printf(self, x):
        print x


class ProfileDialog(QDialog, ui_profileDialog.Ui_DifficultyDialog):
    def __init__(self, parent=None):
        super(ProfileDialog, self).__init__(parent)
        self.setupUi(self)
        self.profile = ''
        self.new = False
        self.selectExistingButton.clicked.connect(self.selectExisting)
        self.createNewButton.clicked.connect(self.createNew)

    def selectExisting(self):
        selectProfileDialog = SelectProfileDialog(self)
        if selectProfileDialog.exec_():
            self.profile = selectProfileDialog.profileDropdown.currentText()
            self.new = False
            self.accept()

    def createNew(self):
        newProfileDialog = NewProfileDialog(self)
        if newProfileDialog.exec_():
            self.profile = newProfileDialog.lineEdit.text()
            self.new = True
            self.accept()


class SelectProfileDialog(QDialog, ui_selectProfileDialog.Ui_SelectProfileDialog):
    def __init__(self, parent=None):
        super(SelectProfileDialog, self).__init__(parent)
        self.setupUi(self)
        profiles = os.listdir('data\\profiles')
        profiles = list(map(QString, profiles))
        self.profileDropdown.addItems(profiles)
        self.profileDropdown.currentIndexChanged.connect(self.comboSpeaker)


    def comboSpeaker(self, index):
        speech.say(self.profileDropdown.itemText(index))


class NewProfileDialog(QDialog, ui_newProfileDialog.Ui_NewProfileDialog):
    def __init__(self, parent=None):
        super(NewProfileDialog, self).__init__(parent)
        self.setupUi(self)


class DifficultyDialog(QDialog, ui_difficultyDialog.Ui_DifficultyDialog):
    def __init__(self, parent=None):
        super(DifficultyDialog, self).__init__(parent)
        self.setupUi(self)
        self.difficulty = ''
        self.easyButton.clicked.connect(self.setAndExit1)
        self.mediumButton.clicked.connect(self.setAndExit2)
        self.hardButton.clicked.connect(self.setAndExit3)

    def setAndExit1(self):
        difficulty = 'easy'
        self.difficulty = difficulty
        self.close()

    def setAndExit2(self):
        difficulty = 'medium'
        self.difficulty = difficulty
        self.close()

    def setAndExit3(self):
        difficulty = 'hard'
        self.difficulty = difficulty
        self.close()


class HighscoresDialog(QDialog, ui_highscoresDialog.Ui_Highscores):
    def __init__(self, parent=None):
        super(HighscoresDialog, self).__init__(parent)
        self.setupUi(self)
        self.readScores()
        i = 1
        for item in self.scores:
            self.listWidget.addItem(QString('%i. %s. Score : %i' % (i, item, self.scores[item][1])))
            i += 1
        self.listWidget.setCurrentItem(self.listWidget.item(0))
        speech.say(str(self.listWidget.currentItem().text()) + '.')
        self.listWidget.currentRowChanged.connect(self.speakItem)

    def speakItem(self):
        speech.say(str(self.listWidget.currentItem().text()) + '.')


    def readScores(self):
        f = open('data\\highscores.txt')
        lines = f.readlines()
        scores = OrderedDict()
        # print(lines)
        i = 0
        while i < (len(lines)):
            profile = lines[i].rstrip()
            infiScore = int(lines[i + 1].rstrip())
            timeScore = int(lines[i + 2].rstrip())
            i = i + 4
            scores[profile] = (infiScore, timeScore)
        self.scores = scores.copy()
        f.close()


class HelpWindow(QMainWindow, ui_helpWindow.Ui_HelpWindow):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.generalHelp, SIGNAL('clicked()'), self.speakGeneralHelp)
        self.connect(self.backButton, SIGNAL('clicked()'), self.goBack)
        self.connect(self.playingHelp, SIGNAL('clicked()'), self.speakPlayingHelp)
        self.connect(self.scoringHelp, SIGNAL('clicked()'), self.speakScoringHelp)
        self.connect(self.startWindowShortcuts, SIGNAL('clicked()'), self.speakStartWindowShortcuts)
        self.connect(self.gameWindowShortcuts, SIGNAL('clicked()'), self.speakGameWindowShortcuts)

    def goBack(self):
        self.hide()
        self.parent().show()

    def speakGeneralHelp(self):
        helpText = """Use tab to select the buttons, and Spacebar or Enter to select. Most buttons also have a shortcut."""
        speech.say(helpText)

    def speakPlayingHelp(self):
        helpText = """The objective of the game is to unscramble a word. There are two modes - untimed, in which you have all the time you need to figure out the answer, and timed where you must answer in 30 seconds."""
        speech.say(helpText)

    def speakScoringHelp(self):
        helpText = """Every time you solve a word, your score increases by one. Every time you try an incorrect answer, or run out of time, the score is set to zero again."""
        speech.say(helpText)

    def speakStartWindowShortcuts(self):
        helpText = """New Game : Alt-N. New Timed Game : Alt-T. Change Profile : Alt-Pee. Select Difficulty : Alt-D. Highscores : Alt-I. Help : Alt-H. Exit : Alt-X."""
        speech.say(helpText)

    def speakGameWindowShortcuts(self):
        helpText = """Home Screen : Alt-H. Repeat the scrambled word: Alt-R. Next word : Alt-N. Check Answer : Alt-C."""
        speech.say(helpText)

class PlayWindow(QMainWindow, ui_playWindow.Ui_PlayWindow):
    def __init__(self, profile, timed, parent=None):
        super(PlayWindow, self).__init__(parent)
        # self.parent = parent
        self.setupUi(self)
        self.profile = profile
        self.resultLabel.clear()
        self.profileLabel.setText(QString(self.profile.name))
        self.difficultyLabel.setText(QString(self.profile.difficulty))

        if timed:
            self.countdownTime = 30
            self.timer = QTimer(self)
            self.remainingTime = 30
            self.connect(self.timer, SIGNAL('timeout()'), self.timeoutHandler)
            self.secondTimer = QTimer(self)
            self.elapsedSeconds = 0
            self.connect(self.secondTimer, SIGNAL('timeout()'), self.updateTimeLabel)
            self.timeLabel.setText(QString('0'))
        else:
            self.countdownTime = -1
            self.timeLabel.setText(QString('----'))
        self.scoreLabel.setText(QString('Score : 0'))
        self.makewords('data\\words\\' + str(self.profile.difficulty))
        self.resetWord()

        self.connect(self.lineEdit, SIGNAL('returnPressed()'), self.checker)
        self.connect(self.checkButton, SIGNAL('clicked()'), self.checker)
        self.connect(self.repeatButton, SIGNAL('clicked()'), self.speakScrambledWord)
        self.connect(self.nextButton, SIGNAL('clicked()'), self.skipWord)
        self.connect(self.homeButton, SIGNAL('clicked()'), self.goBack)

    def updateTimeLabel(self):
        self.elapsedSeconds += 1
        self.timeLabel.setText(QString(str(self.elapsedSeconds)))
        self.secondTimer.start(1000)

    def timeoutHandler(self):
        speech.say("Timeout")
        self.resetWord()

    def checker(self):
        speech.say("Checking...")
        scrambled = self.scrambledLabel.text()
        cand = self.lineEdit.text()
        validPerm = sorted(scrambled) == sorted(cand)
        validWord = self.isWord(cand)
        if validPerm and validWord:
            self.resultLabel.setText("Correct!")
            speech.say("Correct")
            score = int(self.scoreLabel.text()[8:])
            score = score + 1
            if self.countdownTime > 0:
                self.profile.timeScore = str(max(int(self.profile.timeScore), score))
            else:
                self.profile.infiScore = str(max(int(self.profile.infiScore), score))
            self.scoreLabel.setText('Score : ' + str(score))

            self.profile.blaclist.add(QString(cand))
            self.resetWord()
            self.lineEdit.clear()
            self.lineEdit.setFocus()
        else:
            # self.resultLabel.setText("Wrong! Right answer is " + self.answer)
            # speech.say("Wrong! Right answer is " + self.answer)
            self.resultLabel.setText('Wrong!')
            speech.say('Wrong!')
            self.scoreLabel.setText('Score : 0')
            self.lineEdit.clear()
            self.lineEdit.setFocus()

    def resetWord(self):
        newWord = random.choice(tuple(self.words))
        self.answer = newWord
        newWord = self.scrambleWord(newWord)
        self.scrambledLabel.setText(newWord)
        self.speakScrambledWord()
        self.lineEdit.setFocus()
        if self.countdownTime > 0:
            self.elapsedSeconds = 0
            self.timer.start(self.countdownTime * 1000)
            self.secondTimer.start(1000)


    def speakScrambledWord(self):
        s = str(self.scrambledLabel.text())
        speech.say("Unscramble : ")
        for char in s:
            speech.say(char + '...')
            # speech.say(phrase)
        self.lineEdit.setFocus()

    def skipWord(self):
        self.scoreLabel.setText('Score : 0')
        self.resetWord()

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
            cand = QString(line.rstrip())
            if cand not in self.profile.blaclist:
                wordset.add(cand)
        self.words = wordset

    def isWord(self, cand):
        """

        :rtype : bool
        """
        if cand in self.words:
            # print('found', cand)
            return True
        else:
            # print('not found', cand)
            return False

    def goBack(self):
        self.hide()
        self.parent().profile = self.profile
        self.parent().show()


# class TimedPlayWindow(PlayWindow):
# def __init__(self, profile, parent=None):
#         super(TimedPlayWindow, self).__init__(profile, parent)
#         self.countdownTime = 30


class FocusButton(QPushButton):
    def __init__(self, parent=None):
        super(FocusButton, self).__init__(parent)

    tabSignal = pyqtSignal()

    def focusInEvent(self, QFocusEvent):
        self.emit(SIGNAL('tabSignal()'))


class Profile:
    def __init__(self, name, difficulty, infiScore, timeScore, blacklist):
        assert isinstance(blacklist, set)
        self.name = name
        self.difficulty = difficulty
        self.infiScore = infiScore
        self.timeScore = timeScore
        self.blaclist = blacklist.copy()


def makewords(wordfile):
    wordfile = open(wordfile)
    wordset = set()
    for line in wordfile:
        wordset.add(QString(line.rstrip()))
    wordfile.close()
    return wordset


def main():
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    # playWindow.scrambledLabel.setText("itioncompet")
    # print('competition' in playWindow.words)
    # assert isinstance(startWindow.newButton, ui_startWindow.FocusButton)
    startWindow.show()
    app.exec_()


main()