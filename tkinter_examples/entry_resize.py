import tkinter as tk


root = tk.Tk()
root.title("Resizing entry boxes")
root.geometry("400x400")


def myClick():
    hello = "Hello " + entry.get()
    myLabel = tk.Label(root, text=hello)
    myLabel.pack(pady=10)
    entry.delete(0, "end")


entry = tk.Entry(root, width=20, font="Helvetica, 12")
entry.pack(padx=10, pady=10, ipady=10)

button = tk.Button(root, text="Enter Your Name", command=myClick)
button.pack(pady=10)


# root.mainloop()
