# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profileDialog.ui'
#
# Created: Sun Dec 28 18:16:56 2014
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
        self.selectExistingButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.selectExistingButton.setFont(font)
        self.selectExistingButton.setObjectName(_fromUtf8("selectExistingButton"))
        self.verticalLayout.addWidget(self.selectExistingButton)
        self.createNewButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createNewButton.setFont(font)
        self.createNewButton.setObjectName(_fromUtf8("createNewButton"))
        self.verticalLayout.addWidget(self.createNewButton)
        self.cancelButton = QtGui.QPushButton(DifficultyDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout.addWidget(self.cancelButton)

        self.retranslateUi(DifficultyDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), DifficultyDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DifficultyDialog)

    def retranslateUi(self, DifficultyDialog):
        DifficultyDialog.setWindowTitle(_translate("DifficultyDialog", "Change Profile", None))
        self.selectExistingButton.setText(_translate("DifficultyDialog", "Select Existing Profile", None))
        self.createNewButton.setText(_translate("DifficultyDialog", "Create New Profile", None))
        self.cancelButton.setText(_translate("DifficultyDialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DifficultyDialog = QtGui.QDialog()
    ui = Ui_DifficultyDialog()
    ui.setupUi(DifficultyDialog)
    DifficultyDialog.show()
    sys.exit(app.exec_())

