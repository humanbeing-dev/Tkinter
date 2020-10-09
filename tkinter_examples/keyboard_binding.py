import tkinter as tk

# root = tk.Tk()
# root.title("Keyboard binding")
# root.geometry("300x300")


class Binder:
    def __init__(self, master=None):
        self.master = master
        self.myButton = tk.Button(master, text="Click Me")
        self.myButton.pack(pady=20)
        # self.myButton.bind("<Button-3>", self.clicker) # PPM
        # self.myButton.bind("<Enter>", self.clicker)    # Podczas najechania
        # self.myButton.bind("<Leave>", self.clicker)    # Podczas zjechania
        # self.myButton.bind("<FocusIn>", self.clicker)  # Po tab
        # self.myButton.bind("<Return>", self.clicker)  # After enter
        self.myButton.bind("<Key>", self.clicker)  # After enter

    def clicker(self, event):
        print(dir(event))
        myLabel = tk.Label(self.master, text=f"You clicked button {event.char} {event.x}, {event.y}")
        myLabel.pack()

#

# root = tk.Tk()
# root.title("Tkinter Classes")
# root.geometry("300x300")
#
#
# class TestingClasses:
#     def __init__(self, master):
#         myFrame = tk.Frame(master)
#         myFrame.pack()
#
#         self.myButton = tk.Button(master, text="Click Me!", command=self.clicker)
#         self.myButton.pack(pady=20)
#
#     def clicker(self):
#         print("It's not very ambitious, but it's nice to start using classes")
#
#

root = tk.Tk()
root.title("Binding")
root.geometry("300x300")
app = Binder()
root.mainloop()
