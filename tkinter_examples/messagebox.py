from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("MessageBox example")
root.iconbitmap("logo.ico")


def popup():
    response = messagebox.askquestion("This is my popup", "Co tam?")
    Label(root, text=response).pack()
    if response == "yes":
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no!").pack()


Button(root, text="popup", command=popup).pack()


root.mainloop()
