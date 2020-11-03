from tkinter import *
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.w = 600
        self.h = 400
        self.x = self.w//2
        self.y = self.h//2
        self.create_widgets()

    def create_widgets(self):
        self.my_canvas = Canvas(self, width=self.w, height=self.h, bg="white")
        self.my_canvas.pack()
        global img
        img = Image.open("images/login_button.jpg")
        img = img.resize((102, 34))
        img = ImageTk.PhotoImage(img)

        self.my_image = self.my_canvas.create_image(self.w/2, self.h/2, image=img)
        self.master.bind("<B1-Motion>", self.pressing)
        self.lbl_1 = Label(self, text='')
        self.lbl_1.pack()
        self.lbl_2 = Label(self, text='')
        self.lbl_2.pack()

    def pressing(self, event):
        global img
        img = Image.open("images/login_button.jpg")
        img = img.resize((102, 34))
        img = ImageTk.PhotoImage(img)

        self.my_image = self.my_canvas.create_image(event.x, event.y, image=img)
        self.lbl_1.config(text=f"x = {event.x}")
        self.lbl_2.config(text=f"y = {event.y}")
        # self.my_canvas.move(self.my_image, event.x, event.y)


root = Tk()
root.title("ProMCS")
root.geometry("800x600")
app = Application(master=root)
app.mainloop()
