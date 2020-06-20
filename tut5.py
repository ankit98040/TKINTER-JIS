from tkinter import *

root = Tk()

root.geometry("655x365")
root.title("Button GUI")

f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN, padx = 90)
f1.pack(side = TOP, anchor = "nw", fill = X)

def hello():
    print("Hey welcome to Tkinter")

def dj():
    print("OOH LALA ")


b1 = Button(f1, fg = "red", text = "print now", command = hello, padx = 10)
b1.pack(side = LEFT)

b2 = Button(f1, fg = "red", text = "print b2", padx = 10, command = dj)
b2.pack(side = LEFT)

b3 = Button(f1, fg = "red", text = "print b3", padx = 10)
b3.pack(side = LEFT)

b4 = Button(f1, fg = "red", text = "print b4", padx = 10)
b4.pack(side = LEFT)

root.mainloop()