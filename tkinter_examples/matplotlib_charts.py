from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Charts')
# root.iconbitmap('logo.ico')
root.geometry("640x520")


def graph():
    house_prices = np.random.normal(200000, 250000, 5000)
    plt.hist(house_prices, 50)
    plt.savefig(fname='test.png')
    f = Image.open('test.png')
    global img
    img = ImageTk.PhotoImage(f)
    lbl = Label(root, image=img)
    lbl.grid(row=1, column=0)


button = Button(root, text="Show graph", command=graph).grid(row=0, column=0)

root.mainloop()
