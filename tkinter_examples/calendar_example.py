from tkinter import *
from tkcalendar import *
from datetime import date


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.today = date.today()
        self.create_widgets()

    def create_widgets(self):
        self.my_button = Button(self, text="Get Date", command=self.grab_date)
        self.my_button.pack()
        self.my_label = Label(self, text="")
        self.my_label.pack()
        self.cal = Calendar(self, selectmode="day", year=self.today.year, month=self.today.month, day=self.today.day)
        self.cal.pack()

    def grab_date(self):
        self.my_label.config(text=f'{self.cal.get_date()}')


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
