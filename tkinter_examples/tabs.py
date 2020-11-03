from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.my_notebook = ttk.Notebook(self.master)
        self.my_notebook.pack()
        self.my_frame1 = Frame(self.my_notebook, width=400, height=400, bg="blue")
        self.my_frame2 = Frame(self.my_notebook, width=400, height=400, bg="red")
        self.my_frame1.pack(fill="both", expand=1)
        self.my_frame2.pack(fill="both", expand=1)
        self.my_notebook.add(self.my_frame1, text="Blue")
        self.my_notebook.add(self.my_frame2, text="Red")
        self.my_button = Button(self.my_frame1, text="Hide Tab 2", command=self.hide)
        self.my_button.pack()

    def hide(self):
        self.my_notebook.hide(1)


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
