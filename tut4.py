from tkinter import *
root = Tk()

root.title("FRAME GUI")
root.geometry("640x540")

f1 = Frame(root, bg = "green", borderwidth = 6, padx = 10, relief = SUNKEN)
f1.pack(side = LEFT, anchor = "nw",fill = "y")

f2 = Frame(root, bg = "blue", borderwidth = 8, relief=SUNKEN)
f2.pack(side = TOP, fill = "x")

l = Label(f2,text = "My text editor", font = "Helvetica 16 bold", fg = "red")
l.pack(pady = 20)

l = Label(f1,text = "Project python")
l.pack(pady= 70)



root.mainloop()