from tkinter import *

root = Tk()
root.title("ProMCS")
root.geometry("400x400")


def something():
    my_label.config(text="New text")
    root.config(bg="blue")
    my_button.config(text="Second")
    my_button.config(state=DISABLED)


my_label = Label(root, text="This is my text", font=("Helvetica", 32))
my_label.pack(pady=10)

my_button = Button(root, text="Click Me", command=something)
my_button.pack(pady=10)

root.mainloop()
