from tkinter import *
from PIL import ImageTk, Image
from random import choice, shuffle, choices
import os


root = Tk()
root.title("Flashcards")
root.geometry("700x580")
voivodeships = [file[:-4] for file in os.listdir("./img")]
capital = StringVar()
capital.set(NONE)
voivos = {"dolnośląskie": "Wrocław",
          "kujawsko-pomorskie": "Bydgoszcz",
          "lubelskie": "Lublin",
          "lubuskie": "Gorzów Wielkopolski",
          "łódzkie": "Łódź",
          "małopolskie": "Kraków",
          "mazowieckie": "Warszawa",
          "opolskie": "Opole",
          "podkarpackie": "Rzeszów",
          "podlaskie": "Białystok",
          "pomorskie": "Gdańsk",
          "śląskie": "Katowice",
          "świętokrzyskie": "Kielce",
          "warmińsko-mazurskie": "Olsztyn",
          "wielkopolskie": "Poznań",
          "zachodniopomorskie": "Szczecin"}


# Check the answer
def check_answer(frame, correct_answer, your_answer):
    print(correct_answer, your_answer)
    if your_answer.lower() == correct_answer.lower():
        message = Label(frame, text="Correct answer!!!", fg="#16d010").pack()
    else:
        message = Label(frame, text=f"Wrong answer. It is {correct_answer}.", fg="red").pack()


# Create State Flashcard Function
def states():
    hide_all_frames()
    state_frame.pack(fill=BOTH, expand=1)
    global state_img
    chosen_state = choice(voivodeships)
    state_img = ImageTk.PhotoImage(Image.open(f'img/{chosen_state}.jpg'))
    show_state = Label(state_frame, image=state_img).pack()
    lbl_answer = Label(state_frame, text="Type your answer below:").pack()
    answer = Entry(state_frame, text="Type you answer here...", width=18)
    answer.pack(ipady=4)
    check = Button(state_frame, text="Check you answer", width=15,
                   command=lambda: check_answer(state_frame, chosen_state, answer.get())).pack()
    # lbl = Label(state_frame, text=chosen_state).pack()
    btn = Button(state_frame, text="Draw next", command=states, width=15).pack(pady=7)
    answer.delete(0, END)


# Create State Flashcard Function
def capitals():
    hide_all_frames()
    capitals_frame.pack(fill=BOTH, expand=1)
    global state_img
    chosen_state = choice(voivodeships)
    capitals_list = [voivos[chosen_state]]
    temp = list(voivos.values())
    temp.remove(voivos[chosen_state])
    shuffle(temp)
    capitals_list.extend(temp[:2])
    shuffle(capitals_list)
    state_img = ImageTk.PhotoImage(Image.open(f'img/{chosen_state}.jpg'))
    show_state = Label(capitals_frame, image=state_img).pack()
    my_label = Label(capitals_frame, text="What is the capital of the voivodeship above?").pack()
    for cap in capitals_list:
        radio = Radiobutton(capitals_frame, text=cap, variable=capital, width=25, value=cap).pack(side=TOP)
    check = Button(capitals_frame, text="Check you answer", width=15,
                   command=lambda: check_answer(capitals_frame, voivos[chosen_state], capital.get())).pack()
    btn = Button(capitals_frame, text="Draw next", command=capitals, width=15).pack(pady=7)


def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    capitals_frame.pack_forget()


# Create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capitals", command=capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
math_menu.add_command(label="Adding", command=states)
math_menu.add_command(label="Multiplying", command=capitals)


# Create our Frames
state_frame = Frame(root, width=500, height=500)
capitals_frame = Frame(root, width=500, height=500)



root.mainloop()

