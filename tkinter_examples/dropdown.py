from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
# root.iconbitmap("logo.ico")


clicked = StringVar()
clicked.set("Monday")

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
    ]

drop = OptionMenu(root, clicked, *weekdays).pack()


root.mainloop()
