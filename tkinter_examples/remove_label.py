import tkinter as tk

root = tk.Tk()
root.title("Removing labels")
root.geometry("300x300")


def remove_label():
    myLabel.pack_forget()
    # myLabel.destroy()
    # myLabel.grid_forget()
    button1['state'] = tk.NORMAL
    button2['state'] = tk.DISABLED
    print(button1.winfo_exists())


def myClick():
    hello = "Hello " + entry.get()
    global myLabel
    myLabel = tk.Label(root, text=hello)
    myLabel.pack(pady=10)
    entry.delete(0, "end")
    button1['state'] = tk.DISABLED
    button2['state'] = tk.NORMAL


entry = tk.Entry(root, width=20, font="Helvetica, 12")
entry.pack(padx=10, pady=4, ipady=10)

button1 = tk.Button(root, text="Enter Your Name", command=myClick)
button1.pack(pady=4)
button2 = tk.Button(root, text="Clean", command=remove_label)
button2.pack(pady=4)

root.mainloop()
