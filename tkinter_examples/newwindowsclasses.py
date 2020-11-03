from tkinter import *
from tkinter.ttk import *


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()


master = Tk()
master.geometry("200x200")

label = Label(master, text="This is the main window")
label.pack(side=TOP, pady=10)

btn = Button(master, text="Click to open a new window")
btn.bind("<Button>", lambda e: NewWindow(master))
btn.pack(pady=10)

mainloop()
