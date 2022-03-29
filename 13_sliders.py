from tkinter import *

win = Tk()
win.title("sliders")
win.iconbitmap(None)
win.geometry("400x400")


def sliders():
    my_label = Label(win, text=horizontal.get()).pack()
    win.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# by default it's(sliders) a vertical
vertical = Scale(win, from_=0, to=400)
vertical.pack()

# create horizontal slider
horizontal = Scale(win, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# my_label = Label(win,text=horizontal.get()).pack()
btn = Button(win, text="Click here", command=sliders).pack()

win.mainloop()
