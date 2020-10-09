from tkinter import *

root = Tk()
# root.title("Calculator")

e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=4)


def button_click(sign):
    # e.delete(0, END)
    e.insert(END, sign)
    return


def button_clear(sign):
    e.delete(0, END)
    return


def button_equal(sign):
    val = eval(e.get())
    e.delete(0, END)
    e.insert(0, val)


def button_del(sign):
    index = len(e.get()) - 1
    e.delete(index, END)


# Define buttons
btn_sign = ["/", "*", "-", "+",
            7, 8, 9, "sqrt",
            4, 5, 6, "pow",
            1, 2, 3, "C",
            0, ".", "DEL", "="]

# Define commands
btn_command = [
    button_click
] * 15 + [button_clear] + [button_click] * 2 + [button_del, button_equal]


for index, sign in enumerate(btn_sign):
    row = 1 + index // 4
    column = index % 4
    width = 6
    columnspan = 1

    btn = Button(root, text=sign, width=width, pady=20, command=lambda s=sign, i=index: btn_command[i](s))
    btn.grid(row=row, column=column, columnspan=columnspan)

root.mainloop()
