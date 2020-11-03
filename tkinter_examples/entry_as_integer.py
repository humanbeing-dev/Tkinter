from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def number(self):
        try:
            int(self.ent_1.get())
            self.lbl_2.config(text=f"{self.ent_1.get()} is a number")
        except ValueError:
            self.lbl_2.config(text=f"{self.ent_1.get()} is NOT a number!")
        finally:
            self.ent_1.delete(0, END)

    def create_widgets(self):
        self.lbl_1 = Label(self, text="Enter a Number")
        self.lbl_1.pack()
        self.ent_1 = Entry(self)
        self.ent_1.pack()
        self.btn_1 = Button(self, text="Enter a Number", command=self.number)
        self.btn_1.pack()
        self.lbl_2 = Label(self, text="")
        self.lbl_2.pack()


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
