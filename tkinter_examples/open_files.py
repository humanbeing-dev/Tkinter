from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import pathlib, os

root = Tk()
root.title("Loading files")
root.iconbitmap("logo.ico")
start_path = pathlib.Path().absolute()


def load_file():
    global my_image

    file = filedialog.askopenfilenames(
        initialdir=start_path,
        title="Select a file",
        filetypes=(("png files", "*.png"),
                   ("txt files", "*.txt"),
                   ("all files", "*")))

    print(file)
    print(dir(os))
    print(os.path.basename(file[0]))
    print(os.path.splitext(os.path.basename(file[0])))
    my_label = Label(root, text=file).pack()
    # my_image = ImageTk.PhotoImage(Image.open(file))
    # my_image_label = Label(image=my_image).pack()


btn = Button(root, text="Load a file", command=load_file)
btn.pack()

root.mainloop()
