from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.entries = []
        self.create_widgets()
        self.entry_list = ""

    def create_widgets(self):
        for i in range(5):
            for j in range(5):
                self.entry = Entry(self, width=15)
                self.entry.grid(row=j, column=i)
                self.entries.append(self.entry)

        self.btn = Button(self, text="Click Me", command=self.something).grid(column=0)
        self.lbl = Label(self, text="test")
        self.lbl.grid(column=0)

    def something(self):
        for entry in self.entries:
            self.entry_list += str(entry.get())+"\n"

        self.lbl.config(text=self.entry_list)



root = Tk()
root.title("ProMCS")
root.geometry("800x200")
app = Application(master=root)
app.mainloop()
