# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created: Sun Dec 28 15:35:59 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName(_fromUtf8("startWindow"))
        startWindow.resize(845, 600)
        startWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(startWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.newButton.setFont(font)
        self.newButton.setAutoDefault(True)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.verticalLayout.addWidget(self.newButton)
        self.newTimedButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.newTimedButton.setFont(font)
        self.newTimedButton.setAutoDefault(True)
        self.newTimedButton.setObjectName(_fromUtf8("newTimedButton"))
        self.verticalLayout.addWidget(self.newTimedButton)
        self.profileButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.profileButton.setFont(font)
        self.profileButton.setAutoDefault(True)
        self.profileButton.setObjectName(_fromUtf8("profileButton"))
        self.verticalLayout.addWidget(self.profileButton)
        self.difficultyButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.difficultyButton.setFont(font)
        self.difficultyButton.setAutoDefault(True)
        self.difficultyButton.setObjectName(_fromUtf8("difficultyButton"))
        self.verticalLayout.addWidget(self.difficultyButton)
        self.highscoresButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.highscoresButton.setFont(font)
        self.highscoresButton.setAutoDefault(True)
        self.highscoresButton.setObjectName(_fromUtf8("highscoresButton"))
        self.verticalLayout.addWidget(self.highscoresButton)
        self.helpButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.helpButton.setFont(font)
        self.helpButton.setAutoDefault(True)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.verticalLayout.addWidget(self.helpButton)
        self.exitButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setAutoDefault(True)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.verticalLayout.addWidget(self.exitButton)
        startWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(startWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        startWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(startWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        startWindow.setStatusBar(self.statusbar)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)
        startWindow.setTabOrder(self.newButton, self.newTimedButton)
        startWindow.setTabOrder(self.newTimedButton, self.profileButton)
        startWindow.setTabOrder(self.profileButton, self.difficultyButton)
        startWindow.setTabOrder(self.difficultyButton, self.highscoresButton)
        startWindow.setTabOrder(self.highscoresButton, self.helpButton)
        startWindow.setTabOrder(self.helpButton, self.exitButton)

    def retranslateUi(self, startWindow):
        startWindow.setWindowTitle(_translate("startWindow", "Unscramblify", None))
        self.newButton.setText(_translate("startWindow", "&New Game", None))
        self.newTimedButton.setText(_translate("startWindow", "New &Timed Game", None))
        self.profileButton.setText(_translate("startWindow", "Change &Profile", None))
        self.difficultyButton.setText(_translate("startWindow", "Select &Difficulty", None))
        self.highscoresButton.setText(_translate("startWindow", "H&ighscores", None))
        self.helpButton.setText(_translate("startWindow", "&Help", None))
        self.exitButton.setText(_translate("startWindow", "E&xit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    startWindow = QtGui.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())

