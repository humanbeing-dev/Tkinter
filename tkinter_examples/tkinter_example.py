from tkinter import *
import platform

root = Tk()
root.title("Program do konwersji plików TXT do CSV")

if platform.system() == "Windows":
    root.iconbitmap("logo.ico")

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name: ")


def myClick():
    name = e.get()
    if name:
        text = f"Your name is: {name}"
    else:
        text = "You haven't written any fucking name."

    myLabel = Label(root, text=text)
    myLabel.pack()


myButton1 = Button(root, text="Wybierz plik TXT do konwersji", width=40, pady=20, command=myClick)
myButton2 = Button(root, text="Konwertuj plik do CSV", width=40, pady=20)
myButton3 = Button(root, text="Wyjście", width=40, pady=20)

myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()
