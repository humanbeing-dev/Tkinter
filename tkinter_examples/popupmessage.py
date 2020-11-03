from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.defaultbg = self.master.cget('bg')
        print(self.defaultbg)

    def create_widgets(self):
        self.my_button = Button(self.master, text="Click Me", font=("Helvetica, 28"))
        self.my_button.pack(pady=50)

        self.lbl = Label(self.master, text="test", bd=1, relief=SUNKEN, anchor=E)
        self.lbl.pack(fill=X, side=BOTTOM, ipady=2)

        self.my_button.bind("<Enter>", self.button_hover)
        self.my_button.bind("<Leave>", self.button_leave)

    def button_hover(self, e):
        self.my_button["bg"] = "white"
        self.lbl.config(text="I'm Hovering Over The Button!!")

    def button_leave(self, e):
        self.my_button["bg"] = self.defaultbg
        self.lbl.config(text="Test")


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
