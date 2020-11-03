import tkinter as tk

root = tk.Tk()
root.title("Special characters")
root.geometry("400x400")


my_label_1 = tk.Label(root, text=f'42\u00b0', font=("Helvetica", 32))
my_label_1.pack()
my_label_2 = tk.Label(root, text=f'MS\u00A9', font=("Helvetica", 32))
my_label_2.pack()
my_label_3 = tk.Label(root, text=f'\u00BB', font=("Helvetica", 32))
my_label_3.pack()


root.mainloop()
