# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playWindow.ui'
#
# Created: Sat Dec 13 00:49:37 2014
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

class Ui_PlayWindow(object):
    def setupUi(self, PlayWindow):
        PlayWindow.setObjectName(_fromUtf8("PlayWindow"))
        PlayWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PlayWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 31, 551, 491))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.checkButton = QtGui.QPushButton(self.widget)
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.gridLayout.addWidget(self.checkButton, 3, 1, 1, 1)
        self.scrambledLabel = QtGui.QLabel(self.widget)
        self.scrambledLabel.setObjectName(_fromUtf8("scrambledLabel"))
        self.gridLayout.addWidget(self.scrambledLabel, 0, 0, 1, 1)
        self.resultLabel = QtGui.QLabel(self.widget)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.gridLayout.addWidget(self.resultLabel, 2, 0, 1, 1)
        PlayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PlayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PlayWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PlayWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PlayWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlayWindow)
        QtCore.QMetaObject.connectSlotsByName(PlayWindow)

    def retranslateUi(self, PlayWindow):
        PlayWindow.setWindowTitle(_translate("PlayWindow", "MainWindow", None))
        self.checkButton.setText(_translate("PlayWindow", "Check!", None))
        self.scrambledLabel.setText(_translate("PlayWindow", "TextLabel", None))
        self.resultLabel.setText(_translate("PlayWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PlayWindow = QtGui.QMainWindow()
    ui = Ui_PlayWindow()
    ui.setupUi(PlayWindow)
    PlayWindow.show()
    sys.exit(app.exec_())

