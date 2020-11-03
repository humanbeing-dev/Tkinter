from tkinter import *
import pygame


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_1 = Button(self, text="Play", width=15, font=("Helvetica, 28"), command=self.play)
        self.btn_1.pack()
        self.btn_2 = Button(self, text="Stop", width=15, font=("Helvetica, 28"), command=self.stop)
        self.btn_2.pack()

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load("audio/mario.mp3")
        pygame.mixer.music.play(loops=0)

    def stop(self):
        pygame.mixer.init()
        pygame.mixer.music.stop()

root = Tk()
root.title("ProMCS")
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
