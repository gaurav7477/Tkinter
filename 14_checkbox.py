from tkinter import *

win = Tk()
win.title("sliders")
win.iconbitmap(None)


def check_():
    my_label = Label(win, text=var.get()).pack()


# for integer

# var = IntVar()
# c = Checkbutton(win, text="check button", variable=var)
# c.pack()

# for string

var = StringVar()

# it's a by default check and if we click the button nothing happened ->> i don't know why
# so I have used deselect then it's work properly
c = Checkbutton(win, text="would you like to start learn by code_with_gaurav:) ! check here", variable=var, onvalue="Welcome to code_with_gaurav", offvalue="it's ok")
c.deselect()
c.pack()

btn = Button(win, text="click button", command=check_).pack()

win.mainloop()
