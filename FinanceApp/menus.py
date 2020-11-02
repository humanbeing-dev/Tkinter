import tkinter as tk
from tkinter import colorchooser


def file_new(root):
    file_new_frame = tk.Frame(root, width=400, height=400, bg="red")
    file_new_frame.pack(fill="both", expand=1)


def set_background_color(root):
    picked_color = colorchooser.askcolor()
    with open("config.ini", "w") as f:
        f.write(picked_color[1])
    root.config(bg=picked_color[1])


def set_colors(root):
    options_window = tk.Tk()
    options_window.title("Options")
    options_window.geometry("300x300")

    options_frame = tk.Frame(options_window)
    options_frame.pack()
    lbl_1 = tk.Label(options_frame, text="Change color:")
    lbl_1.grid(row=0, column=0)
    btn_1 = tk.Button(options_frame, text="Pick color", command=lambda: set_background_color(root))
    btn_1.grid(row=0, column=1)
    # lbl = tk.Label(options_window, text=)

    #
    # new_colors_frame = tk.Frame(root, width=400, height=400)
    # new_colors_frame.pack(fill="both", expand=1)
    # r = 250
    # g = 250
    # b = 250
    # root.config(bg=f"#{r:x}{g:x}{b:x}")
    #


def set_menus(root):
    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New...", command=lambda: file_new(root))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    edit_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command=root.quit)
    edit_menu.add_command(label="Copy", command=root.quit)

    option_menu = tk.Menu(my_menu)
    my_menu.add_cascade(label="Options", menu=option_menu)
    option_menu.add_command(label="Change color", command=lambda: set_colors(root))
