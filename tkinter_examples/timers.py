from tkinter import *
import datetime
import time


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        now = datetime.datetime.now()
        self.timer = Label(text=now.strftime("%H:%M:%S"), font=("Helvetica, 32"))
        self.timer.pack()
        self.weekday = Label(text=now.strftime("%A"), font=("Helvetica, 32"))
        self.weekday.pack()

    def update_time(self):
        now = datetime.datetime.now()
        self.timer.config(text=now.strftime("%H:%M:%S"))
        self.weekday.config(text=now.strftime("%A"))
        self.update_idletasks()
        self.timer.after(1, self.update_time)


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
