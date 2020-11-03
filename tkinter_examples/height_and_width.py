from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_button = Button(self, text="Click Me", command=self.cmd_info)
        self.my_button.pack()

    def cmd_info(self):
        self.dimension_label = Label(self, text=self.master.winfo_geometry())
        self.dimension_label.pack()



root = Tk()
root.title("ProMCS")
root.geometry("400x400+40+40")
app = Application(master=root)
app.mainloop()
