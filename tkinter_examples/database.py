from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Sliders")
root.iconbitmap("logo.ico")
root.geometry("300x500")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Commit Changes
conn.commit()

# Create table
# c.execute("""CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )""")

# Create Text Boxes
text_boxes = ["first_name", "last_name", "address", "city", "state", "zipcode"]
labels = ["First name:", "Last name:", "Address:", "City:", "State:", "Zipcode:"]

for index, label in enumerate(labels):
    lbl = Label(root, text=label, width=10, name=f"label_{str(index)}")
    lbl.grid(row=index, column=0, padx=10, pady=((10, 0) if index == 0 else 0))

for index, column in enumerate(text_boxes):
    text_box = Entry(root, width=30, name=column)
    text_box.grid(row=index, column=1, padx=10, pady=((10, 0) if index == 0 else 0))

delete_label = Label(root, text="ID to delete", width=10).grid(row=12, column=0, padx=10)
delete_entry = Entry(root, width=30, name="delete")
delete_entry.grid(row=12, column=1, padx=10)

edit_label = Label(root, text="ID to edit", width=10).grid(row=10, column=0, padx=10)
edit_entry = Entry(root, width=30, name="edit")
edit_entry.grid(row=10, column=1, padx=10)


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:first_name,:last_name,:address,:city,:state,:zipcode)", {
        'first_name': root.children[text_boxes[0]].get(),
        'last_name': root.children[text_boxes[1]].get(),
        'address': root.children[text_boxes[2]].get(),
        'city': root.children[text_boxes[3]].get(),
        'state': root.children[text_boxes[4]].get(),
        'zipcode': root.children[text_boxes[5]].get(),
    })
    conn.commit()
    conn.close()

    [root.children[tb].delete(0, END) for tb in text_boxes]
    query()


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)
    print_records = ""

    for record in records:
        print_records += f"{record[6]} {record[0]} {record[1]}\n"

    query_label = Label(root, text=print_records).grid(row=13, column=0, columnspan=2)

    # c.fetchone()
    # c.fetchmany()
    conn.commit()
    conn.close()


def update(editor, oid):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute(f"""UPDATE addresses SET 
        "first_name" = :first_name,
        "last_name" = :last_name,
        "address" = :address,
        "city" = :city,
        "state" = :state,
        "zipcode" = :zipcode
        
        WHERE oid = {oid}""", {
            'first_name': editor.children[text_boxes[0]].get(),
            'last_name': editor.children[text_boxes[1]].get(),
            'address': editor.children[text_boxes[2]].get(),
            'city': editor.children[text_boxes[3]].get(),
            'state': editor.children[text_boxes[4]].get(),
            'zipcode': editor.children[text_boxes[5]].get(),
    })
    conn.commit()
    conn.close()
    editor.destroy()


def edit_record(oid):
    editor = Tk()
    editor.title("Update a record")
    editor.iconbitmap("logo.ico")
    editor.geometry("300x200")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM addresses WHERE oid={oid}")
    records = c.fetchone()
    conn.commit()
    conn.close()

    for index, label in enumerate(labels):
        lbl = Label(editor, text=label, width=10, name=f"label_{str(index)}")
        lbl.grid(row=index, column=0, padx=10, pady=((10, 0) if index == 0 else 0))

    for index, column in enumerate(text_boxes):
        text_box = Entry(editor, width=30, name=column)
        text_box.grid(row=index, column=1, padx=10, pady=((10, 0) if index == 0 else 0))
        text_box.insert(0, records[index])

    save_btn = Button(editor, text="Save Record",command=lambda editor=editor, oid=oid: update(editor, oid), width=30)
    save_btn.grid(row=6, column=0, columnspan=2)


def delete_record():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute(f"DELETE from addresses WHERE oid={delete_entry.get()}")
    conn.commit()
    conn.close()

    [root.children[tb].delete(0, END) for tb in text_boxes]
    query()


submit_btn = Button(root, text="Add record to DB", command=submit, width=30).grid(row=6, column=0, columnspan=2, pady=(10, 0))
query_btn = Button(root, text="Read record from DB", command=query, width=30).grid(row=7, column=0, columnspan=2)
edit_btn = Button(root, text="Edit record from DB", command=lambda: edit_record(edit_entry.get()), width=30).grid(row=8, column=0, columnspan=2)
delete_btn = Button(root, text="Delete record from DB", command=delete_record, width=30).grid(row=11, column=0, columnspan=2, pady=(0, 10))


# Close Connection
conn.close()

root.mainloop()
