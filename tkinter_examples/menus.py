import tkinter as tk

root = tk.Tk()
root.title("Testing Menus")
root.geometry("400x400")

my_menu = tk.Menu(root)
root.config(menu=my_menu)


def our_command():
    pass


# Create a menu item
file_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu item
edit_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="Copy", command=our_command)


root.mainloop()
