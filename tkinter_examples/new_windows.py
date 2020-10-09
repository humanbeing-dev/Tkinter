from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("New windows")
root.iconbitmap("logo.ico")


def new_window():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap("logo.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/agile.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="open Second Window", command=new_window).pack()


mainloop()
