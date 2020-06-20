from tkinter import *

root = Tk()

photo = PhotoImage(file="images.png")
lab = Label(image=photo)
lab.pack()

root.mainloop()