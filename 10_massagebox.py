from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('messagebox')
win.iconbitmap("Images/umbrella-academy-theme-cj2.jpg")


def popup():
    # responses = messagebox.showinfo("this is my popup","hello world!")
    # responses = messagebox.showwarning("this is my popup","don't do this")
    # responses = messagebox.showerror("this is my popup", "error")
    # responses = messagebox.askquestion("this is my popup", "are you happy")
    # responses = messagebox.askyesno("this is my popup", "are you ready")
    responses = messagebox.askokcancel("this is my popup", "hello")
    Label(win,text=responses).pack()

    if responses == 1:
        Label(win,text="you clicked ok").pack()

    else:
        Label(win,text="you clicked cancel").pack()


Button(win, text="popup", command=popup).pack()
win.mainloop()
