from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
# root.iconbitmap("logo.ico")
root.geometry("400x400")

vertical = Scale(root, from_=200, to=400)
vertical.pack()

horizontal = Scale(root, from_=200, to=400, orient=HORIZONTAL)
horizontal.pack()
my_label = Label(root, text=horizontal.get()).pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


my_btn = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()
