import tkinter as tk

root = tk.Tk()
root.title("Tkinter Classes")
root.geometry("300x300")


class TestingClasses:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.pack()

        self.myButton = tk.Button(master, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("It's not very ambitious, but it's nice to start using classes")


app = TestingClasses(root)
root.mainloop()
