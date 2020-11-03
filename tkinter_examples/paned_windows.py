from tkinter import *

root = Tk()
root.title("Paned windows")
root.geometry("400x400")

# Panels
panel_1 = PanedWindow(bd=.05, bg="black", width=500)
panel_1.pack(fill=BOTH, expand=1)
left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)
panel_1.config(width=500)

# panel_2 = PanedWindow(bd=.05, bg="black")
# panel_2.pack(fill=BOTH, expand=1)
# left_label = Label(panel_2, text="Middle Panel")
# panel_2.add(left_label)

# Second panel
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=.05, bg="black")
panel_1.add(panel_2)

# top = Label(panel_2, text="Label top")
# panel_2.add(top)
# middle = Label(panel_2, text="Label middle")
# panel_2.add(middle)
bottom = Label(panel_2, text="Label bottom")
panel_2.add(bottom)

# left_label = Label(panel_1, text="Left Panel")
# panel_2.add(left_label)


root.mainloop()
