from tkinter import *

win = Tk()
win.title("grid")

# myLabel1  = Label(win,text= "hi gaurav")
# myLabel2  = Label(win,text= "how ary you")

# ## first way

# myLabel1.grid(row = 0,column = 0)
# myLabel2.grid(row = 1,column = 0)

# ## second way

myLabel1 = Label(win, text="hi gaurav").grid(row=0, column=0)
myLabel2 = Label(win, text="how ary you").grid(row=1, column=0)

win.mainloop()
