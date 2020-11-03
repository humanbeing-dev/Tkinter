from tkinter import *
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_pic = Image.open("images/CAP.png")
        w = self.my_pic.width
        h = self.my_pic.height
        fac = .2
        self.my_pic = self.my_pic.resize((int(w*fac), int(h*fac)), Image.ANTIALIAS)
        self.my_pic = ImageTk.PhotoImage(self.my_pic)


        self.my_lbl = Label(self, image=self.my_pic)
        self.my_lbl.pack()


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
