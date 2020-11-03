from tkinter import *
from tkinter import ttk
import time


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.bar = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
        self.bar.pack(pady=10)

        self.btn_1 = Button(self, text="Step", command=self.step)
        self.btn_1.pack()
        self.btn_2 = Button(self, text="Stop", command=self.stop)
        self.btn_2.pack()
        self.lbl_1 = Label(self, text="0%")
        self.lbl_1.pack()

    def step(self):
        for x in range(10):
            self.bar['value'] += 10
            self.lbl_1.config(text=f"{self.bar['value']}%")
            self.update_idletasks()
            time.sleep(.5)
        # self.bar.start(10)

    def stop(self):
        # self.bar['value'] += 10
        self.bar.stop()


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
