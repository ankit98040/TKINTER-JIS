from tkinter import *

root = Tk()
root.title('Entry widget and Grid layout')
root.geometry("640x436")

def getvals():
    print(uservalue.get())
    print(passvalue.get())

f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN, padx = 90)
f1.pack(side = TOP, anchor = "nw", fill = X)

username= Label(f1, text = "Username", padx = 30)
#username.pack(pady = 10)
username.grid()

password= Label(f1, text = "Password" , padx = 30)
#password.pack(pady = 10)
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(f1, textvariable = uservalue)
passentry = Entry(f1, textvariable = passvalue)

userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)

Button(f1, text='Submit', command = getvals).grid()

root.mainloop()