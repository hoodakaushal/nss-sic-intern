# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'difficultyDialog.ui'
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


class Ui_DifficultyDialog(object):
    def setupUi(self, DifficultyDialog):
        DifficultyDialog.setObjectName(_fromUtf8("DifficultyDialog"))
        DifficultyDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DifficultyDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.easyButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.easyButton.setFont(font)
        self.easyButton.setObjectName(_fromUtf8("easyButton"))
        self.verticalLayout.addWidget(self.easyButton)
        self.mediumButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mediumButton.setFont(font)
        self.mediumButton.setObjectName(_fromUtf8("mediumButton"))
        self.verticalLayout.addWidget(self.mediumButton)
        self.hardButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.hardButton.setFont(font)
        self.hardButton.setObjectName(_fromUtf8("hardButton"))
        self.verticalLayout.addWidget(self.hardButton)

        self.retranslateUi(DifficultyDialog)
        QtCore.QMetaObject.connectSlotsByName(DifficultyDialog)

    def retranslateUi(self, DifficultyDialog):
        DifficultyDialog.setWindowTitle(_translate("DifficultyDialog", "Select Difficulty", None))
        self.label.setText(_translate("DifficultyDialog", "Select Difficulty", None))
        self.easyButton.setText(_translate("DifficultyDialog", "&Easy", None))
        self.mediumButton.setText(_translate("DifficultyDialog", "&Medium", None))
        self.hardButton.setText(_translate("DifficultyDialog", "&Hard", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    DifficultyDialog = QtGui.QDialog()
    ui = Ui_DifficultyDialog()
    ui.setupUi(DifficultyDialog)
    DifficultyDialog.show()
    sys.exit(app.exec_())

