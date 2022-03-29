from tkinter import *

win = Tk()
win.title("Button")


def buttonClick():
    myLabel = Label(win, text="look I Clicked a Button")
    myLabel.pack()


# whenever we called the function in python we added a parenthesis
# command =buttonClick ->> add () ->> produce error
myButton = Button(win, text="clicked button", command=buttonClick, bg="blue", fg="yellow", padx=50, pady=40)

# myButton = Button(win,text = "look I Clicked a Button")

# myButton = Button(win,text = "click button", padx = 50, pady = 50)

myButton.pack()

win.mainloop()
