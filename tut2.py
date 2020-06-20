from tkinter import *
from PIL import Image, ImageTk
#python image library
#imagetk supports jpg image

a1 = Tk()

a1.geometry("455x244")

#for png image
#photo = PhotoImage(file="filename.png")
#a2 = Label(image = photo)
#a2.pack()

image = Image.open("PJXlVd.jpg")
photo = ImageTk.PhotoImage(image)


a2 = Label(image = photo)
a2.pack()

a1.mainloop()