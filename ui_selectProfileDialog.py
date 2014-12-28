# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectProfileDialog.ui'
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

class Ui_SelectProfileDialog(object):
    def setupUi(self, SelectProfileDialog):
        SelectProfileDialog.setObjectName(_fromUtf8("SelectProfileDialog"))
        SelectProfileDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(SelectProfileDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.selectProfileLabel = QtGui.QLabel(SelectProfileDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(True)
        self.selectProfileLabel.setFont(font)
        self.selectProfileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectProfileLabel.setObjectName(_fromUtf8("selectProfileLabel"))
        self.verticalLayout.addWidget(self.selectProfileLabel)
        self.profileDropdown = QtGui.QComboBox(SelectProfileDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.profileDropdown.setFont(font)
        self.profileDropdown.setObjectName(_fromUtf8("profileDropdown"))
        self.verticalLayout.addWidget(self.profileDropdown)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(SelectProfileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SelectProfileDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SelectProfileDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SelectProfileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectProfileDialog)

    def retranslateUi(self, SelectProfileDialog):
        SelectProfileDialog.setWindowTitle(_translate("SelectProfileDialog", "Dialog", None))
        self.selectProfileLabel.setText(_translate("SelectProfileDialog", "Select Profile", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SelectProfileDialog = QtGui.QDialog()
    ui = Ui_SelectProfileDialog()
    ui.setupUi(SelectProfileDialog)
    SelectProfileDialog.show()
    sys.exit(app.exec_())

