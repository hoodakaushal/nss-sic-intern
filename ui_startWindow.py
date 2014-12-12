# # -*- coding: utf-8 -*-
#
# # Form implementation generated from reading ui file 'startWindow.ui'
# #
# # Created: Fri Dec 12 17:17:31 2014
# #      by: PyQt4 UI code generator 4.11.3
# #
# # WARNING! All changes made in this file will be lost!
#
# from PyQt4 import QtCore, QtGui
#
# try:
# _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
#
# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)
#
# class Ui_startWindow(object):
#     def setupUi(self, startWindow):
#         startWindow.setObjectName(_fromUtf8("startWindow"))
#         startWindow.resize(845, 600)
#         startWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.centralwidget = QtGui.QWidget(startWindow)
#         self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
#         self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
#         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
#         self.verticalLayout = QtGui.QVBoxLayout()
#         self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
#         self.newButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.newButton.setFont(font)
#         self.newButton.setObjectName(_fromUtf8("newButton"))
#         self.verticalLayout.addWidget(self.newButton)
#         self.profileButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.profileButton.setFont(font)
#         self.profileButton.setObjectName(_fromUtf8("profileButton"))
#         self.verticalLayout.addWidget(self.profileButton)
#         self.wordsetButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.wordsetButton.setFont(font)
#         self.wordsetButton.setObjectName(_fromUtf8("wordsetButton"))
#         self.verticalLayout.addWidget(self.wordsetButton)
#         self.difficultyButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.difficultyButton.setFont(font)
#         self.difficultyButton.setObjectName(_fromUtf8("difficultyButton"))
#         self.verticalLayout.addWidget(self.difficultyButton)
#         self.highscoresButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.highscoresButton.setFont(font)
#         self.highscoresButton.setObjectName(_fromUtf8("highscoresButton"))
#         self.verticalLayout.addWidget(self.highscoresButton)
#         self.helpButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.helpButton.setFont(font)
#         self.helpButton.setObjectName(_fromUtf8("helpButton"))
#         self.verticalLayout.addWidget(self.helpButton)
#         self.exitButton = QtGui.QPushButton(self.centralwidget)
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         font.setBold(True)
#         font.setWeight(75)
#         self.exitButton.setFont(font)
#         self.exitButton.setObjectName(_fromUtf8("exitButton"))
#         self.verticalLayout.addWidget(self.exitButton)
#         self.horizontalLayout.addLayout(self.verticalLayout)
#         startWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtGui.QMenuBar(startWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
#         self.menubar.setObjectName(_fromUtf8("menubar"))
#         startWindow.setMenuBar(self.menubar)
#         self.statusbar = QtGui.QStatusBar(startWindow)
#         self.statusbar.setObjectName(_fromUtf8("statusbar"))
#         startWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(startWindow)
#         QtCore.QMetaObject.connectSlotsByName(startWindow)
#         startWindow.setTabOrder(self.profileButton, self.wordsetButton)
#         startWindow.setTabOrder(self.wordsetButton, self.difficultyButton)
#         startWindow.setTabOrder(self.difficultyButton, self.highscoresButton)
#         startWindow.setTabOrder(self.highscoresButton, self.helpButton)
#         startWindow.setTabOrder(self.helpButton, self.exitButton)
#
#     def retranslateUi(self, startWindow):
#         startWindow.setWindowTitle(_translate("startWindow", "Unscramblify", None))
#         self.newButton.setText(_translate("startWindow", "New Game", None))
#         self.profileButton.setText(_translate("startWindow", "Change Profile", None))
#         self.wordsetButton.setText(_translate("startWindow", "Select Wordset", None))
#         self.difficultyButton.setText(_translate("startWindow", "Select Difficulty", None))
#         self.highscoresButton.setText(_translate("startWindow", "Highscores", None))
#         self.helpButton.setText(_translate("startWindow", "Help", None))
#         self.exitButton.setText(_translate("startWindow", "Exit", None))
#
#
# if __name__ == "__main__":
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     startWindow = QtGui.QMainWindow()
#     ui = Ui_startWindow()
#     ui.setupUi(startWindow)
#     startWindow.show()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created: Fri Dec 12 17:17:31 2014
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


class FocusButton(QtGui.QPushButton):
    def __init__(self, parent=None):
        super(FocusButton, self).__init__(parent)

    tabSignal = QtCore.pyqtSignal()

    def focusInEvent(self, QFocusEvent):
        self.emit(QtCore.SIGNAL('tabSignal()'))


class Ui_startWindow(object):
    def setupUi(self, startWindow):
        startWindow.setObjectName(_fromUtf8("startWindow"))
        startWindow.resize(845, 600)
        startWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(startWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.newButton.setFont(font)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.verticalLayout.addWidget(self.newButton)
        self.profileButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.profileButton.setFont(font)
        self.profileButton.setObjectName(_fromUtf8("profileButton"))
        self.verticalLayout.addWidget(self.profileButton)
        self.wordsetButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.wordsetButton.setFont(font)
        self.wordsetButton.setObjectName(_fromUtf8("wordsetButton"))
        self.verticalLayout.addWidget(self.wordsetButton)
        self.difficultyButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.difficultyButton.setFont(font)
        self.difficultyButton.setObjectName(_fromUtf8("difficultyButton"))
        self.verticalLayout.addWidget(self.difficultyButton)
        self.highscoresButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.highscoresButton.setFont(font)
        self.highscoresButton.setObjectName(_fromUtf8("highscoresButton"))
        self.verticalLayout.addWidget(self.highscoresButton)
        self.helpButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.helpButton.setFont(font)
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.verticalLayout.addWidget(self.helpButton)
        self.exitButton = FocusButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.verticalLayout.addWidget(self.exitButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        startWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(startWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        startWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(startWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        startWindow.setStatusBar(self.statusbar)

        self.retranslateUi(startWindow)
        QtCore.QMetaObject.connectSlotsByName(startWindow)
        startWindow.setTabOrder(self.profileButton, self.wordsetButton)
        startWindow.setTabOrder(self.wordsetButton, self.difficultyButton)
        startWindow.setTabOrder(self.difficultyButton, self.highscoresButton)
        startWindow.setTabOrder(self.highscoresButton, self.helpButton)
        startWindow.setTabOrder(self.helpButton, self.exitButton)

    def retranslateUi(self, startWindow):
        startWindow.setWindowTitle(_translate("startWindow", "Unscramblify", None))
        self.newButton.setText(_translate("startWindow", "New Game", None))
        self.profileButton.setText(_translate("startWindow", "Change Profile", None))
        self.wordsetButton.setText(_translate("startWindow", "Select Wordset", None))
        self.difficultyButton.setText(_translate("startWindow", "Select Difficulty", None))
        self.highscoresButton.setText(_translate("startWindow", "Highscores", None))
        self.helpButton.setText(_translate("startWindow", "Help", None))
        self.exitButton.setText(_translate("startWindow", "Exit", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    startWindow = QtGui.QMainWindow()
    ui = Ui_startWindow()
    ui.setupUi(startWindow)
    startWindow.show()
    sys.exit(app.exec_())

