from tkinter import *
from PIL import ImageTk, Image


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.update_image("images/login_button.jpg")

        self.my_label = Label(self, image=img)
        self.my_label.pack()
        self.my_label.bind("<Enter>", self.change)
        self.my_label.bind("<Leave>", self.leave)

    def change(self, e):
        self.update_image("images/CAP.png")
        self.my_label.config(image=img)

    def leave(self, e):
        self.update_image("images/login_button.jpg")
        self.my_label.config(image=img)

    @staticmethod
    def update_image(image_path):
        global img
        img = Image.open(image_path)
        img = img.resize((102, 34))
        img = ImageTk.PhotoImage(img)
        return img


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
