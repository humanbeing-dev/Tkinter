from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_canvas = Canvas(self, width=300, height=200, bg="white")
        self.my_canvas.pack()
        self.my_canvas.create_rectangle(50, 150, 250, 50, fill="pink")
        self.my_canvas.create_oval(50, 150, 250, 50, fill="cyan")
        self.my_canvas.create_line(0, 100, 300, 100, fill="red")
        self.my_canvas.create_line(150, 200, 150, 0, fill="red")


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
