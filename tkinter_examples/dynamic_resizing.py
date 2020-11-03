from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def resize(self):
        self.master.geometry("500x500")
        self.master.update()
        print(self.master.winfo_height())
        print(self.master.winfo_width())

    def create_widgets(self):
        self.my_button = Button(self, text="Resize", command=self.resize)
        self.my_button.pack(pady=20)


root = Tk()
root.title("ProMCS")
root.geometry("800x800")
app = Application(master=root)
app.mainloop()
