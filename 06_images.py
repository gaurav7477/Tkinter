from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images')
root.iconbitmap("images/batman-dark-theme-vo1.jpg")

pdf_pic = Image.open("../PdfConverter/logo2.jpg")
# pic_resize = pdf_pic.resize((500, 300))
my_img = ImageTk.PhotoImage(pdf_pic)

my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
