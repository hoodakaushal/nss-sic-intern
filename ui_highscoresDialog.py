# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'highscoresDialog.ui'
#
# Created: Sun Dec 28 18:40:43 2014
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

class Ui_Highscores(object):
    def setupUi(self, Highscores):
        Highscores.setObjectName(_fromUtf8("Highscores"))
        Highscores.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Highscores)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listWidget = QtGui.QListWidget(Highscores)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Highscores)
        QtCore.QMetaObject.connectSlotsByName(Highscores)

    def retranslateUi(self, Highscores):
        Highscores.setWindowTitle(_translate("Highscores", "Dialog", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Highscores = QtGui.QDialog()
    ui = Ui_Highscores()
    ui.setupUi(Highscores)
    Highscores.show()
    sys.exit(app.exec_())

