from tkinter import *

root = Tk()
root.title("Simple radio buttons")
# root.iconbitmap("logo.ico")

pizza = StringVar()
pizza.set(NONE)

MODES = [
    "Pepperoni",
    "Vesuvio",
    "Onion",
    "Cheese"
]


def clicked():
    myLabel['text'] = f"You have chosen {pizza.get()} pizza"


for taste in MODES:
    Radiobutton(root, text=taste, variable=pizza, value=taste, command=clicked).pack(anchor=W)

myLabel = Label(root, text=f"You have chosen {pizza.get()} pizza")
myLabel.pack()

root.mainloop()
