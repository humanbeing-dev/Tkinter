from tkinter import *
from PIL import ImageTk, Image
import os

counter = 0

root = Tk()
root.geometry("1500x1000")
root.title("Simple image_viewer")
# root.iconbitmap('logo.ico')

img_list = [img for img in os.listdir("images") if os.path.splitext(img)[1] in [".png", ".jpg", '.jpeg']]
img_counter = len(img_list)

image = Image.open(f"images/{img_list[counter]}")
print(image.height)

max_height = 500

if image.height > max_height:
    height = max_height
    height_ratio = image.height/max_height
    width = round(image.width / height_ratio)
    print(width)
    image = image.resize((width, max_height))

my_img = ImageTk.PhotoImage(image)

my_label = Label(root, image=my_img, width=1490, height=930)
my_label.grid(row=0, column=0, columnspan=3)


def next_img():
    global counter
    counter += 1
    counter = counter % img_counter
    my_img = ImageTk.PhotoImage(Image.open(f"images/{img_list[counter]}"))


    my_label.configure(image=my_img)
    my_label.image = my_img
    my_footer['text'] = (f"Image {counter+1} of {img_counter}")


def prev_img():
    global counter
    counter -= 1
    counter = counter if counter >= 0 else (img_counter - 1)
    my_img = ImageTk.PhotoImage(Image.open(f"images/{img_list[counter]}"))
    my_label.configure(image=my_img)
    my_label.image = my_img
    my_footer['text'] = (f"Image {counter+1} of {img_counter}")


btn_next = Button(text=">>", command=next_img, width=20, pady=10)
btn_exit = Button(text="EXIT", command=root.quit, width=20, pady=10)
btn_prev = Button(text="<<", command=prev_img, width=20, pady=10)

btn_next.grid(row=1, column=2)
btn_exit.grid(row=1, column=1)
btn_prev.grid(row=1, column=0)

my_footer = Label(text=f"Image {counter+1} of {img_counter}", bd=1, relief=SUNKEN, anchor=E)
my_footer.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
