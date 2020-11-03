from tkinter import *
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(master)

    def create_widgets(self, master):
        global img
        img = Image.open("images/login_button.jpg")
        img = img.resize((102, 34))
        img = ImageTk.PhotoImage(img)

        self.my_button = Button(master, image=img, command=self.thing, borderwidth=0)
        self.my_button.pack(pady=20)
        self.my_label = Label(self, text='Test')
        self.my_label.pack()
    #
    def thing(self):
        self.my_label.config(text="Nice click")


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
