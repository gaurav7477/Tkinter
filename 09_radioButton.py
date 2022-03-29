from tkinter import *

root = Tk()
root.title('RadioButton')
root.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")

# for integer variable

# r = IntVar()
# r.set("2")
#
# Radiobutton(root, text="Option 1", variable=r, value=1).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2).pack()
#
# # my_Label = Label(root, text=r.get())
# # my_Label.pack()
#
#
# def clicked(value):
#     my_label = Label(root, text=value)
#     my_label.pack()
#
#
# myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
# myButton.pack()


TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    my_Label = Label(root, text=value)
    my_Label.pack()


# myLabel = Label(root, text=pizza.get())
# myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
