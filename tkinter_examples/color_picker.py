from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color picker")
root.geometry("400x400")


def change_background_color():
    root.config(bg=colorchooser.askcolor()[1])


btn = Button(root, text="Pick color", command=change_background_color)
btn.pack()

root.mainloop()
