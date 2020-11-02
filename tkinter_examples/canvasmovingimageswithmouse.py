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

        self.my_image = self.my_canvas.create_image(0, 0, anchor=NW, image=img)


        # self.my_circle = self.my_canvas.create_oval(self.x, self.y, self.x+10, self.y+10)
        self.master.bind("<Key>", self.pressing)
        # self.coorx = Label(self, text=f"x = {(self.my_canvas.coords(self.my_circle)[0] + self.my_canvas.coords(self.my_circle)[2])/2}")
        # self.coorx.pack()
        # self.coory = Label(self, text=f"y = {(self.my_canvas.coords(self.my_circle)[1] + self.my_canvas.coords(self.my_circle)[3])/2}")
        # self.coory.pack()

    def pressing(self, event):
        x = 0
        y = 0
        if event.keysym == "Left": x = -10
        if event.keysym == "Right": x = 10
        if event.keysym == "Up": y = -10
        if event.keysym == "Down": y = 10
        self.my_canvas.move(self.my_image, x, y)
        # self.coorx.config(text=f"x = {(self.my_canvas.coords(self.my_circle)[0] + self.my_canvas.coords(self.my_circle)[2])/2}")
        # self.coory.config(text=f"y = {(self.my_canvas.coords(self.my_circle)[1] + self.my_canvas.coords(self.my_circle)[3])/2}")


root = Tk()
root.title("ProMCS")
root.geometry("800x600")
app = Application(master=root)
app.mainloop()
