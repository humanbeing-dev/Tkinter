# pip install pyttsx3

from tkinter import *
import pyttsx3


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ent = Entry(self, font="Helvetica, 16")
        self.ent.pack()

        self.btn = Button(self, text="Speech", command=self.speech)
        self.btn.pack()

    def speech(self):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'polish')
        engine.say(self.ent.get())
        self.ent.delete(0, END)
        engine.runAndWait()


root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
