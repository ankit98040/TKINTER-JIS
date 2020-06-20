from tkinter import *

a = Tk()

a.geometry("500x400")
t = Label(text = "READY", bg = "red", fg = "green", padx = 90, pady = 115)
t.pack(side = BOTTOM, fill = Y, pady = 60)

a.mainloop()