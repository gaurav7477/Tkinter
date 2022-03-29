from tkinter import *

root = Tk()
root.title("sliders")
root.iconbitmap(None)

root.geometry("400x400")


# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

# we can not write ->> variable = clicked,value = options
# put * for show everything
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
