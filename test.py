# __author__ = 'hooda'
#
# from Tkinter import Tk, BOTH, Frame
# from ttk import Button, Style
#
#
# class Example(Frame):
#
# def __init__(self, parent):
#         Frame.__init__(self, parent, background="grey")
#
#         self.parent = parent
#
#         self.initUI()
#         self.centre()
#
#     def centre(self):
#         w = 400
#         h = 300
#
#         sw = self.parent.winfo_screenwidth()
#         sh = self.parent.winfo_screenheight()
#
#         x = (sw - w)/2
#         y = (sh - h)/2
#
#         self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
#
#
#     def initUI(self):
#
#         self.parent.title("Simple")
#         self.pack(fill=BOTH, expand=1)
#
#         self.style = Style()
#         # self.style.theme_use("default")
#
#         quitButton = Button(self, text='GTFO!', command=self.quit)
#         quitButton.place(x=50, y=50)
#
# def main():
#
#     root = Tk()
#     root.geometry("250x150+300+300")
#     app = Example(root)
#     root.mainloop()
#
#
# main()

# from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, \
# QLabel, QVBoxLayout, QWidget
# from PyQt4.QtCore import pyqtSignal
#
#
# class MainWindow1(QMainWindow):
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)
#         button = QPushButton('Test')
#         button.clicked.connect(self.newWindow)
#         label = QLabel('MainWindow1')
#
#         centralWidget = QWidget()
#         vbox = QVBoxLayout(centralWidget)
#         vbox.addWidget(label)
#         vbox.addWidget(button)
#         self.setCentralWidget(centralWidget)
#
#     def newWindow(self):
#         self.mainwindow2 = MainWindow2(self)
#         self.mainwindow2.closed.connect(self.show)
#         self.mainwindow2.show()
#         self.hide()
#
#
# class MainWindow2(QMainWindow):
#     # QMainWindow doesn't have a closed signal, so we'll make one.
#     closed = pyqtSignal()
#
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)
#         self.parent = parent
#         label = QLabel('MainWindow2', self)
#
#     def closeEvent(self, event):
#         self.closed.emit()
#         event.accept()
#
#
# def startmain():
#     app = QApplication(sys.argv)
#     mainwindow1 = MainWindow1()
#     mainwindow1.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     import sys
#
#     startmain()

import speech

# from PyQt4.QtGui import *
# from PyQt4.QtCore import *
# import sys
# class myLCDNumber(QLCDNumber):
# value = 60
#
#   @pyqtSlot()
#   def count(self):
#     self.display(self.value)
#     self.value = self.value-1
#
#
# def main():
#     app 	 = QApplication(sys.argv)
#     lcdNumber	 = myLCDNumber()
#
#     #Resize width and height
#     lcdNumber.resize(250,250)
#     lcdNumber.setWindowTitle('PyQt QTimer Countdown Example')
#     lcdNumber.display(60)
#     timer = QTimer()
#     lcdNumber.connect(timer,SIGNAL("timeout()"),lcdNumber,SLOT("count()"))
#     timer.start(1000)
#
#     lcdNumber.show()
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()

alphabet = ['A.',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z']

# for item in alphabet:
# speech.say(item)
speech.say('x.')