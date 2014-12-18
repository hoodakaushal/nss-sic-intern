# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpWindow.ui'
#
# Created: Thu Dec 18 02:23:25 2014
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.backButton.setFont(font)
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.helpText = QtGui.QTextBrowser(self.centralwidget)
        self.helpText.setObjectName(_fromUtf8("helpText"))
        self.verticalLayout.addWidget(self.helpText)
        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(HelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    HelpWindow = QtGui.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())

