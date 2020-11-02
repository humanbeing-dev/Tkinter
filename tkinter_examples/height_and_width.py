from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        pass


root = Tk()
root.title("ProMCS")
root.geometry("400x400+40+40")
app = Application(master=root)
app.mainloop()
