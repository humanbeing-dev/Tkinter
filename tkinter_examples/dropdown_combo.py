import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Binding dropdown and comboboxes")
root.geometry("400x400")


def day_picked(event):
    text = tk.Label(root, text=clicked.get())
    text.pack()


def comboclick(event):
    text = tk.Label(root, text=combo.get())
    text.pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = tk.StringVar()
clicked.set(options[0])

drop = tk.OptionMenu(root, clicked, *options, command=day_picked)
drop.config(width=10)
drop.pack()

combo = ttk.Combobox(root, value=options)
combo.current(0)
combo.bind("<<ComboboxSelected>>", comboclick)
combo.pack()

# mybutton = tk.Button(root, text="click Me", command=day_picked)
# mybutton.pack()

root.mainloop()
