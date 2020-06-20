from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN, padx = 90)
f1.pack(side = TOP, anchor = "nw", fill = X)

user = Label(f1, text="Username",pady= 30)
password = Label(f1, text="Password", pady= 30)
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(f1, textvariable = uservalue)
passentry = Entry(f1, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(f1, text="Submit", command=getvals, bg='red').grid()

root.mainloop()