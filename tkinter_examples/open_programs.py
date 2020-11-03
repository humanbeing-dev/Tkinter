from tkinter import *
from tkinter import filedialog
import os
import io


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_button = Button(self, text="Open Program", width=15, command=self.open_program)
        self.my_button.pack()
        self.gedit = Button(self, text="Open Gedit", width=15, command=lambda: os.system(f"/usr/bin/gedit"))
        self.gedit.pack()
        self.shutter = Button(self, text="Open Shutter", width=15, command=lambda: os.system(f"/usr/bin/shutter"))
        self.shutter.pack()
        self.my_label = Label(self, text="")
        self.my_label.pack()

    def open_program(self):
        self.my_program = filedialog.askopenfile()
        self.my_label.config(text=self.my_program)
        # print(self.my_program.name)
        os.system(f"{self.my_program.name}")


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
