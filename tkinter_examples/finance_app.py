from tkinter import *
# from PIL import ImageTk, Image
import sqlite3
import datetime

root = Tk()
root.title("Finance app")
root.geometry("350x700")

conn = sqlite3.connect("my_finances.db")
c = conn.cursor()

# Create labels
labels = ['Date:', 'Weekday:', 'Category', 'Subcategory', 'Expenditure']

for index, label in enumerate(labels):
    lbl = Label(root, text=label, width=20, name=f"label_{index}").grid(row=index, column=0)
    ent = Entry(root, width=20, name=f"textbox_{index}").grid(row=index, column=1)


def submit(cat=None):
    conn = sqlite3.connect("my_finances.db")
    c = conn.cursor()

    if not cat:
        c.execute("INSERT INTO expenditures VALUES (:exp_date,:weekday, :category, :subcategory, :expend)", {
            'exp_date': root.children['textbox_0'].get(),
            'weekday': root.children['textbox_1'].get(),
            'category': root.children['textbox_2'].get(),
            'subcategory': root.children['textbox_3'].get(),
            'expend': root.children['textbox_4'].get(),
        })
    else:
        c.execute("INSERT INTO expenditures VALUES (:exp_date,:weekday, :category, :subcategory, :expend)", {
            'exp_date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'weekday': datetime.datetime.now().strftime("%A"),
            'category': cat,
            'subcategory': root.children['textbox_3'].get(),
            'expend': root.children['textbox_4'].get(),
        })

    conn.commit()
    conn.close()
    query()


def query():
    conn = sqlite3.connect("my_finances.db")
    c = conn.cursor()

    records = ''
    c.execute("""SELECT oid, * FROM expenditures""")
    entries = c.fetchall()
    print(entries)
    for entry in entries:
        records += f"{entry[0]} - {entry[1]} - {entry[3]} - {entry[5]}\n"

    lbl = Label(root, text=records).grid(row=10, column=0, columnspan=2)

    conn.commit()
    conn.close()


# Create buttons
btn_submit = Button(root, text="Submit", command=submit, width=20).grid(row=5, column=0, columnspan=2)
btn_query = Button(root, text="Query", command=query, width=20).grid(row=6, column=0, columnspan=2)
btn_food_regular = Button(root, text="Food regular", command=lambda: submit("1-111"), width=20).grid(row=7, column=0, columnspan=2)
btn_food_city = Button(root, text="Food city", command=lambda: submit("1-112"), width=20).grid(row=8, column=0, columnspan=2)
btn_flat = Button(root, text="Flat", command=lambda: submit("1-141"), width=20).grid(row=9, column=0, columnspan=2)

conn.commit()
conn.close()

query()
root.mainloop()
