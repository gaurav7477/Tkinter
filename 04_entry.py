from tkinter import *
from tkinter.messagebox import showinfo

from PyPDF2 import PdfFileWriter, PdfFileReader

win = Tk()


def get_password():
    top = Tk()
    e = Entry(top, width=50)
    e.pack()
    e.insert(0, "password")
    # user_name = name_var.get()

    myButton1 = Button(win, text="encrypted ", command=encrypt_pdf)
    myButton1.pack()


def encrypt_pdf():
    global filenames1, e
    # # top = Toplevel()
    # top = Tk()
    # e = Entry(top, width=60)
    # e.pack()
    # e.insert(0, " password ")

    new = PdfFileWriter()
    file = PdfFileReader(filenames1)
    name = filenames1.replace(".pdf", "_encrypted.pdf")
    num = file.numPages
    for idx in range(num):
        page = file.getPage(idx)
        new.addPage(page)

    password = e.get()
    new.encrypt(password)
    with open(name, "wb") as f:
        new.write(f)
        showinfo("Done", "File successfully Encrypted ")
        f.close()


#
# def clickedButton(name_entry=None):
#     top = Tk()
#     e = Entry(top, width=50)
#     e.pack()
#     e.insert(0, "password")
#
#     name_label = Label(win, text="Enter your password")
#     name_label.grid(row=0, column=0, sticky=W)
#
#     name_var = StringVar()
#     name_entry.grid(row=0, column=1)
#     name_entry = Entry(top, width=16, textvariable=name_var)
#     name_entry.focus()
#
#     button_18 = Button(top, text="okk", fg="red", font=("times new roman", 15, "bold"),
#                        command=get_password(), cursor="hand2")
#     button_18.place(x=1000, y=500)

# hello = e.get()
# myLabel = Label(win, text=hello)
# # myLabel = Label(win, text=e.get())
# myLabel.pack()


myButton = Button(win, text="encrypt pdf ", command=get_password)
myButton.pack()

win.mainloop()
