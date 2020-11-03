from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_box = Entry(self, font=("Helvetica", 28))
        self.my_box.pack()
        self.my_button = Button(self, text="Grab Text", command=self.grab)
        self.my_button.pack()
        self.my_label = Label(self, text="")
        self.my_label.pack()

    def grab(self):
        self.my_label.config(text=self.my_box.get())


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
