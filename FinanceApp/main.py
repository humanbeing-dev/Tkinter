import tkinter as tk
from tkcalendar import *
from tkinter import colorchooser
from FinanceApp.menus import set_menus
from FinanceApp.database_handling import show_databases
from datetime import date


class OurFinances(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("800x400")
        self.master.title("Our family finances")
        self.today = date.today()
        self.set_master_bg()
        self.create_widgets()
        self.create_calendar()

    def set_master_bg(self):
        with open("config.ini") as f:
            self.bg = f.readline()
            self.master.config(bg=self.bg)

    def create_widgets(self):
        self.entries_frame = tk.Frame(self.master, bg=self.bg)
        self.entries_frame.grid(row=0, column=0)

        descriptions = dict(zip(['exp_day', 'exp_cat_1', 'exp_cat_2', 'exp_val'],
                                ['Date:', 'Category:', 'Subcategory:', 'Expenditure:']))

        self.lbl = tk.Label(self.entries_frame, bg=self.bg, text="Entry data")
        self.lbl.grid(row=0, column=0, stick=tk.W)

        for index, key in enumerate(descriptions):
            self.lbl = tk.Label(self.entries_frame, bg=self.bg, text=descriptions[key])
            self.lbl.grid(row=index+1, column=0, stick=tk.W)
            self.ent = tk.Entry(self.entries_frame, name=key)
            self.ent.grid(row=index+1, column=1)

        self.date_spin = tk.Spinbox(self.entries_frame)
        self.date_spin.grid(row=1, column=2)

        print(help(self.date_spin))

        self.entries_frame.children['exp_day'].insert(0, self.today)

    def create_calendar(self):
        # self.my_button = tk.Button(self, text="Get Date", command=self.grab_date)
        # self.my_button.pack()
        # self.my_label = tk.Label(self, text="")
        # self.my_label.pack()
        self.cal = Calendar(self.master, selectmode="day", year=self.today.year, month=self.today.month, day=self.today.day)
        self.cal.grid(row=0, column=2, rowspan=8)
    #
    # def grab_date(self):
    #     self.my_label.config(text=f'{self.cal.get_date()}')


    # def submit(self):
    #     c.execute("INSERT INTO expenditures VALUES (:exp_date,:weekday, :category, :subcategory, :expend)", {
    #         'exp_date': root.children['textbox_0'].get(),
    #         'weekday': root.children['textbox_1'].get(),
    #         'category': root.children['textbox_2'].get(),
    #         'subcategory': root.children['textbox_3'].get(),
    #         'expend': root.children['textbox_4'].get(),
    #     })


#
# def set_background_color():
#     picked_color = colorchooser.askcolor()
#     with open("config.ini", "w") as f:
#         f.write(picked_color[1])
#     root.config(bg=picked_color[1])
#
#
# def insert_labels():
#     dbs = dbs_show()
#     sql_db = ["information_schema", "mysql", "performance_schema", "sys"]
#     for index, db in enumerate(dbs):
#         if db not in sql_db:
#             lbl = tk.Label(root, text=db)
#             lbl.pack()
#
#
# btn_1 = tk.Button(root, text="Show databases", command=insert_labels)
# btn_1.pack()

root = tk.Tk()
app = OurFinances(master=root)
app.mainloop()
