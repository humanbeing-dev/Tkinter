from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
# root.iconbitmap("logo.ico")


def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()
var.set()
c = Checkbutton(root, text="Check this box!", variable=var, onvalue="Tak", offvalue="Nie", command=show)
# c.deselect()
c.pack()

root.mainloop()
