__author__ = 'hooda'

from Tkinter import Tk, BOTH, Frame
from ttk import Button, Style


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="grey")

        self.parent = parent

        self.initUI()
        self.centre()

    def centre(self):
        w = 400
        h = 300

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


    def initUI(self):

        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)

        self.style = Style()
        # self.style.theme_use("default")

        quitButton = Button(self, text='GTFO!', command=self.quit)
        quitButton.place(x=50, y=50)

def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


main()
