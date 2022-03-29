from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Frame")
win.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")

# inside padding
frame = LabelFrame(win, text="this is my frame", padx=100, pady=100)

# outside padding
frame.pack(padx=10, pady=10)

b1 = Button(frame, text="click here")
b2 = Button(frame, text="...or here...")

# we can use both pack,grid
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)


win.mainloop()
