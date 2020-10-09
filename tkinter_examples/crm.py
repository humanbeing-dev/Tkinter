"""Creating CRM - Customer Relationship Managment tool"""

import platform
from tkinter import *
from PIL import Image
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title("Creating CRM")

if platform.system() == "Windows":
    geom = "310x450"
elif platform.system() == "Linux":
    geom = "320x490"
elif platform.system() == "Darwin":
    geom = "350x490"
else:
    geom = "310x450"

root.geometry(geom)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sezamieotworzsie",
    auth_plugin="mysql_native_password",
    database="codemy"
)

my_cursor = mydb.cursor(buffered=True)

label_names = ["First name:", "Last name:", "Zipcode:", "Price:", "Email:", "Address 1:",
               "Address 2:", "City:", "State:", "Country:", "Phone:", "Payment method:", "Discount Code:"]

columns = ["first_name", "last_name", "zipcode", "price_paid", "email", "address_1",
           "address_2", "city", "state", "country", "phone", "payment_method", "discount_code"]

# # Create database
# my_cursor.execute("CREATE DATABASE codemy")
#
# # Remove database
# my_cursor.execute("DROP DATABASE customers")

# # Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db[0].decode("utf-8"))

# Create a table
my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    zipcode INTEGER(10),
    price_paid DECIMAL(10, 2),
    user_id INT AUTO_INCREMENT PRIMARY KEY
)""")

# # ALTER Table
# my_cursor.execute("""ALTER TABLE customers ADD (
#     email VARCHAR(255),
#     address_1 VARCHAR(255),
#     address_2 VARCHAR(255),
#     city VARCHAR(50),
#     state VARCHAR(50),
#     country VARCHAR(255),
#     phone VARCHAR(255),
#     payment_method VARCHAR(50),
#     discount_code VARCHAR(255)
# )""")


# # SHOW TABLES
# my_cursor.execute("SHOW TABLES")
# for tb in my_cursor:
#     print(tb[0].decode('utf-8'))

# # SHOW TABLE
# my_cursor.execute("SELECT * FROM customers")
# for column in my_cursor.description:
#     print(column)


def add_customer():
    values = [root.children[f"textbox_{i}"].get() for i in range(len(label_names))]
    sql_command = f"INSERT INTO customers ({', '.join(columns)}) VALUES {*values,}"
    my_cursor.execute(sql_command)
    mydb.commit()
    clear_fields()


def update_customer(window, id):
    values = [window.children[f"edit_textbox_{i}"].get() for i in range(len(label_names))]
    set_statement = ''
    for index, column in enumerate(columns):
        set_statement += f"{column}='{values[index]}', "
    set_statement = set_statement[:-2]
    sql_command = f"UPDATE customers SET {set_statement} WHERE user_id={id}"
    # print(sql_command)
    my_cursor.execute(sql_command)
    mydb.commit()
    window.destroy()


def clear_fields():
    [root.children[f"textbox_{i}"].delete(0, END) for i in range(len(label_names))]


def edit_record(obj):
    """Function to get value of a user and edit them"""
    # Prepare data
    user_id = (obj._name).split("_")[1]
    sql_command = f"SELECT * FROM customers WHERE user_id={user_id}"
    my_cursor.execute(sql_command)
    result = my_cursor.fetchone()
    result = result[:4] + result[5:]

    # Create edition window
    edition = Tk()
    edition.title("Edit entry")
    edition.geometry(geom)
    # Create a Label
    title_label = Label(edition, text="Edit customer", font="Helvetica, 16")
    title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

    for index, label in enumerate(label_names):
        form_label = Label(edition, text=label, width=15, anchor=W, padx=10).grid(row=index + 1, column=0)
        form_txbox = Entry(edition, width=18, name=f"edit_textbox_{index}")
        form_txbox.grid(row=index + 1, column=1)
        form_txbox.insert(0, result[index])
    save_changes_button = Button(edition, text="Save Changes", width=15, command=lambda: update_customer(edition, user_id)).grid(row=15, column=0)
    cancel_button = Button(edition, text="Cancel", width=15, command=edition.destroy).grid(row=15, column=1)


def list_customers(imp_data=None):
    top = Tk()
    top.title("Second Window")

    csv_button = Button(top, text="Export", command=lambda: to_csv(all_customers)).grid(row=0, column=0)

    if imp_data:
        if type(imp_data) == list:
            all_customers = imp_data
        else:
            lbl = Label(top, text=imp_data)
            lbl.grid(row=0, column=1)
            all_customers = []
    else:
        my_cursor.execute("SELECT * FROM customers")
        all_customers = my_cursor.fetchall()

    def to_csv(data):
        with open('customers.csv', 'a') as f:
            w = csv.writer(f, dialect='excel')
            for row in data:
                row = (row[4],) + row[:4] + row[5:]
                w.writerow(row)

    for column, label in enumerate(["User ID"] + label_names + ["Edit"] + ["Delete"]):
        lbl = Label(top, text=label, width=15).grid(row=1, column=column)
    for index, customer in enumerate(all_customers):
        customer = (customer[4], ) + customer[:4] + customer[5:]
        for column in range(len(["User ID"] + label_names)):
            lbl = Label(top, text=customer[column], width=12).grid(row=2+index, column=column)
        edit_button = Button(top, text="Edit", name=f"edit_{customer[0]}", width=8)
        edit_button.config(command=lambda obj=edit_button: edit_record(obj))
        edit_button.grid(row=2+index, column=len(customer))
        delete_button = Button(top, text="Delete", name=f"delete_{customer[0]}", width=8).grid(row=2+index, column=len(customer)+1)


def search_customers():
    chosen_option = search_combobox.get()
    column_to_search_through = columns[label_names.index(chosen_option)]
    text_to_search = search_customers_txbox.get()

    my_cursor.execute(f"SELECT * FROM customers WHERE {column_to_search_through}='{text_to_search}'")
    results = my_cursor.fetchall()
    results = results if results else f"There is no match in '{chosen_option}' column for '{text_to_search}' value."
    list_customers(results)


# Create a Label
title_label = Label(root, text="Customer database", font=("Helvetica, 16"))
title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

for index, label in enumerate(label_names):
    form_label = Label(root, text=label, width=15, anchor=W, padx=10).grid(row=index+1, column=0)
    form_txbox = Entry(root, width=18, name=f"textbox_{index}").grid(row=index+1, column=1)


column_name = StringVar()
column_name.set(label_names[0])

add_customer_button = Button(root, text="Add Customer", width=15, command=add_customer).grid(row=15, column=0)
clear_fields_button = Button(root, text="Clear Fields", width=15, command=clear_fields).grid(row=15, column=1)
list_customers_button = Button(root, text="List customers", width=15, command=list_customers).grid(row=16, column=0)
search_customers_button = Button(root, text="Search customers", width=15, command=search_customers).grid(row=16, column=1)
# search_customers_check = OptionMenu(root, column_name, *label_names)
# search_customers_check.config(width=13)
# search_customers_check.grid(row=18, column=0)

search_customers_txbox = Entry(root, width=18)
search_customers_txbox.grid(row=17, column=1, ipady=4)
search_combobox = ttk.Combobox(root, value=label_names, width=17)
search_combobox.current(0)
search_combobox.grid(row=17, column=0, ipady=4)

root.mainloop()
