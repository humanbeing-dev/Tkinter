from tkinter import *

root = Tk()
root.title("Program do konwersji plików TXT do CSV")
img = PhotoImage(file="2.png")
root.tk.call('wm', 'iconphoto', root._w, img)
# root.iconbitmap('~/home/maciej/Dev-Projects/TkinterCourse/logo.ico')
# root.iconbitmap(True, "1.png")

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


myButton1 = Button(root, text="Wybierz plik TXT do konwersji", width=50, pady=20, command=myClick)
myButton2 = Button(root, text="Konwertuj plik do CSV", width=50, pady=20)
myButton3 = Button(root, text="Wyjście", width=50, pady=20)

myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()
