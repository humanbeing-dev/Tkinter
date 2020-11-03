from tkinter import *
from random import choice, shuffle


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.words = ['Paint', "Height", "Jumble", 'Show', "Tutorial", "Tkinter"]
        self.create_widgets()
        self.pick_word()

    def create_widgets(self):
        self.lbl_1 = Label(self, text="")
        self.lbl_1.pack()
        self.ent = Entry(self)
        self.ent.pack()
        self.btn = Button(self, text="Check word", command=self.check_word)
        self.btn.pack()
        self.btn_2 = Button(self, text="Hint", command=self.give_hint)
        self.btn_2.pack()
        self.lbl_2 = Label(self, text="")
        self.lbl_2.pack()
        self.lbl_3 = Label(self, text="")
        self.lbl_3.pack()

    def pick_word(self):
        self.word = choice(self.words)
        word_to_shuffle = list(self.word)
        shuffle(word_to_shuffle)
        shuffled_word = "".join(word_to_shuffle)
        self.lbl_1.config(text=shuffled_word)
        self.letters = (letter for letter in self.word)
        self.hint = ""

    def check_word(self):
        if self.ent.get() == self.word:
            self.lbl_2.config(text="Correct answer")
        else:
            self.lbl_2.config(text="Incorrect answer!")

        self.ent.delete(0, END)
        self.lbl_3.config(text="")
        self.pick_word()

    def give_hint(self):
        try:
            self.hint += self.letters.__next__()
        except StopIteration:
            print("End")

        self.lbl_3.config(text=self.hint)



root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
