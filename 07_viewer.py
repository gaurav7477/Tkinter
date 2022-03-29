from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title("Images Viewer")

win.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")

my_image1 = ImageTk.PhotoImage(Image.open("Images/umbrella-academy-theme-cj2.jpg"))
my_image2 = ImageTk.PhotoImage(Image.open("Images/batman-dark-theme-vo1.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("Images/brock-wegner-vMdqDrQk4To-unsplash.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("Images/Lamborghini-Aventador.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("Images/shahin-khalaji-p7MJ8y8gRug-unsplash.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("Images/stephen-andrews-GAkUXHGEc0o-unsplash.jpg"))

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6]
my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

# ## create a status bar

status = Label(win, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


# for forward the images
def forward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(win, text=">>", command=lambda: forward(image_number + 1))
    button_backward = Button(win, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 6:
        button_forward = Button(win, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(win, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# foe backward the images
def backward(image_number):
    global my_label
    global button_forward
    global button_backward

    my_label.grid_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(win, text=">>", command=lambda: forward(image_number + 1))
    button_backward = Button(win, text="<<", command=lambda: backward(image_number - 1))

    if image_number == 1:
        button_back = Button(win, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(win, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# create three button

button_forward = Button(win, text=">>", command=lambda: forward(2))
button_exit = Button(win, text="Exit Program", command=win.quit)
button_backward = Button(win, text="<<", command=backward, state=DISABLED)

# show button on the screen

button_backward.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

win.mainloop()
