# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpWindow.ui'
#
# Created: Sun Dec 28 18:16:55 2014
# by: PyQt4 UI code generator 4.11.3
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

class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName(_fromUtf8("HelpWindow"))
        HelpWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(HelpWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.backButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.backButton.setFont(font)
        self.backButton.setAutoDefault(True)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.verticalLayout.addWidget(self.backButton)
        self.generalHelp = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.generalHelp.setFont(font)
        self.generalHelp.setAutoDefault(True)
        self.generalHelp.setObjectName(_fromUtf8("generalHelp"))
        self.verticalLayout.addWidget(self.generalHelp)
        self.playingHelp = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.playingHelp.setFont(font)
        self.playingHelp.setAutoDefault(True)
        self.playingHelp.setObjectName(_fromUtf8("playingHelp"))
        self.verticalLayout.addWidget(self.playingHelp)
        self.scoringHelp = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.scoringHelp.setFont(font)
        self.scoringHelp.setAutoDefault(True)
        self.scoringHelp.setObjectName(_fromUtf8("scoringHelp"))
        self.verticalLayout.addWidget(self.scoringHelp)
        self.startWindowShortcuts = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.startWindowShortcuts.setFont(font)
        self.startWindowShortcuts.setAutoDefault(True)
        self.startWindowShortcuts.setObjectName(_fromUtf8("startWindowShortcuts"))
        self.verticalLayout.addWidget(self.startWindowShortcuts)
        self.gameWindowShortcuts = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.gameWindowShortcuts.setFont(font)
        self.gameWindowShortcuts.setAutoDefault(True)
        self.gameWindowShortcuts.setObjectName(_fromUtf8("gameWindowShortcuts"))
        self.verticalLayout.addWidget(self.gameWindowShortcuts)
        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        HelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(HelpWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Help", None))
        self.backButton.setText(_translate("HelpWindow", "&Back", None))
        self.generalHelp.setText(_translate("HelpWindow", "General Help", None))
        self.playingHelp.setText(_translate("HelpWindow", "Playing the Game", None))
        self.scoringHelp.setText(_translate("HelpWindow", "Scoring", None))
        self.startWindowShortcuts.setText(_translate("HelpWindow", "Start Window Shortcuts", None))
        self.gameWindowShortcuts.setText(_translate("HelpWindow", "Game Window Shortcuts", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HelpWindow = QtGui.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())

