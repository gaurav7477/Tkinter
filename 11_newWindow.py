from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("my first window ")
win.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")


# create new window
# top = Toplevel()
# top.title("my second window")
# top.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")
# my_img = ImageTk.PhotoImage(Image.open("Images/umbrella-academy-theme-cj2.jpg"))
# my_label = Label(top,image=my_img).pack()


def openWindow():
    global my_img  # it's important to make variable globally
    top = Toplevel()
    top.title("my second window")
    top.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")
    my_img = ImageTk.PhotoImage(Image.open("Images/umbrella-academy-theme-cj2.jpg"))
    my_label = Label(top, image=my_img).pack()

    # for closing window
    btn1 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(win, text="open new window", command=openWindow).pack()

win.mainloop()
