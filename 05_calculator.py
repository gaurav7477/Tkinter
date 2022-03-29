from tkinter import *

win = Tk()
# title
win.title("Calculator")

# create a box for taking a number
e = Entry(win, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


def button_click(numbers):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(numbers))


# for clear box
def button_clear():
    e.delete(0, END)


# for adding
def button__add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


# for subtraction
def button__minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


# for multiplication
def button__into():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


# for division
def button__divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


def button__equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))


# create Button
button_1 = Button(win, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(win, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(win, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(win, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(win, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(win, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(win, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = Button(win, text="clear", padx=40, pady=20, command=button_clear)
button_divide = Button(win, text="/", padx=40, pady=20, command=button__divide)
button_into = Button(win, text="*", padx=40, pady=20, command=button__into)
button_add = Button(win, text="+", padx=40, pady=20, command=button__add)
button_equal = Button(win, text="=", padx=40, pady=20, command=button__equal)
button_minus = Button(win, text="-", padx=40, pady=20, command=button__minus)

# button put on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_divide.grid(row=4, column=2)

button_into.grid(row=1, column=4)
button_minus.grid(row=2, column=4)
button_add.grid(row=3, column=4)
button_equal.grid(row=4, column=4)

win.mainloop()
