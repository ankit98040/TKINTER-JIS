from tkinter import *

#to update the value on the textbox
def click(event):
    #print('hello')
    #pass
    global scvalue
    text = event.widget.cget("text")     #cget to extract text from widget
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())    #eval evaluates a string
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update() #force for updates


root = Tk()
#main loop
root.geometry("600x800")
root.title('Calculator')

#creating the textbox
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10) #internal padding = ipad

#we need to make everything inside this frame
f = Frame(root, bg="grey")
b = Button(f, text="9",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="8",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()





f = Frame(root, bg="grey")
b = Button(f, text="6",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="5",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()




f = Frame(root, bg="grey")
b = Button(f, text="3",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="2",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()







f = Frame(root, bg="grey")
b = Button(f, text="0",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="-",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()






f = Frame(root, bg="grey")
b = Button(f, text="/",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="%",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()






f = Frame(root, bg="grey")
b = Button(f, text="C",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
#to trigger the event, we must bind the button with a function
b.bind("<Button-1>", click)

b = Button(f, text="+",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT, padx = 18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="**",padx=28, pady=18, font="lucida 30 bold")
#b.pack()
b.pack(side=LEFT , padx = 18, pady=5)
b.bind("<Button-1>", click)

f.pack()


root.mainloop()