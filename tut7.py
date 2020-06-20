from tkinter import *

root = Tk()
root.geometry("644x540")
root.title('travel form using Check buttons')
def submitval():
    print('Your data has been successfully submitted. The details are:')
    print(f"NAME = {nameval.get()}")
    print(f"Phone number = {phoneval.get()}")
    print(f"Gender = {genderval.get()}")
    print(f"Emergency Contact = {emergencyval.get()}")
    print(f"Payment mode = {paymentval.get()}")
    print(f"Foodservice = {foodserviceval.get()}")

a = Label(root, text = 'welcome to my travel form', font= "comicsansms 13 bold" , padx = 20, pady = 10, bg = 'blue').grid(row = 0, column = 3)
name = Label(root, text = 'Name', pady = 5)
phone = Label(root, text = 'Phone', pady = 5)
gender = Label(root, text = 'Gender', pady = 5)
emergency = Label(root, text = 'Emergency Contact', pady = 5)
payment = Label(root, text = 'Payment mode', pady = 5)

name.grid(row = 1, column = 2)
phone.grid(row = 2, column = 2)
gender.grid(row = 3, column = 2)
emergency.grid(row = 4, column = 2)
payment.grid(row = 5, column = 2)

nameval = StringVar()
phoneval = StringVar()
genderval = StringVar()
emergencyval = StringVar()
paymentval = StringVar()
foodserviceval = IntVar()

nameentry = Entry(root, textvariable = nameval)
phoneentry = Entry(root, textvariable = phoneval)
genderentry = Entry(root, textvariable = genderval)
emergencyentry = Entry(root, textvariable = emergencyval)
paymententry = Entry(root, textvariable = paymentval)

nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
genderentry.grid(row = 3, column = 3)
emergencyentry.grid(row = 4, column = 3)
paymententry.grid(row = 5, column = 3)

#checkbox

foodservice = Checkbutton(text = 'Want to prebook your meals ? ', variable = foodserviceval)
foodservice.grid(row = 4, column = 4)

#button and function of button

Button(text = 'SUBMIT', command = submitval).grid(row = 5, column = 4)

root.mainloop()