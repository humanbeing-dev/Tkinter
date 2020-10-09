import tkinter as tk
import random

root = tk.Tk()
root.title("Winner generator")
root.geometry("400x400")

entries = [f"contestant_{index}" for index in range(20)]


def pick_winner():
    winner = random.choice(entries)
    winnerLabel = tk.Label(root, text=f"The winner is {winner}")
    winnerLabel.pack()


topLabel = tk.Label(root, text="Winner")
topLabel.pack()

winButton = tk.Button(root, text="Pick a winner!!", command=pick_winner)
winButton.pack()

root.mainloop()
