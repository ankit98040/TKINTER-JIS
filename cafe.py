from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

root = Tk()
root.title('Cafe Management')
root.geometry("1345x845")
root.configure(background = 'black')

tops = Frame(root, width = 1350, height = 100, bd = 14, relief = "raise")
tops.pack(side = TOP)

f1 = Frame(root, width = 900, height = 650, bd = 8, relief = "raise")
f1.pack(side = LEFT)

f2 = Frame(root, width = 440, height = 700, bd = 8, relief = "raise")
f2.pack(side = RIGHT)
#==================================================================================
f1a = Frame(f1, width = 900, height = 330, bd = 8, relief = "raise")
f1a.pack(side = TOP)

f2a = Frame(f1, width = 900, height = 320, bd = 8, relief = "raise")
f2a.pack(side = BOTTOM)
#==================================================================================
ft2 = Frame(f2, width = 440, height = 450, bd = 16, relief = "raise")
ft2.pack(side = TOP)

fb2 = Frame(f2, width = 440, height = 250, bd = 16, relief = "raise")
fb2.pack(side = BOTTOM)
#==================================================================================
f1aa = Frame(f1a, width = 400, height = 330, bd = 8, relief = "raise")
f1aa.pack(side = LEFT)

f1ab = Frame(f1a, width = 400, height = 330, bd = 8, relief = "raise")
f1ab.pack(side = RIGHT)
#==================================================================================
f2aa = Frame(f2a, width = 400, height = 320, bd = 8, relief = "raise")
f2aa.pack(side = LEFT)

f2ab = Frame(f2a, width = 400, height = 320, bd = 8, relief = "raise")
f2ab.pack(side = RIGHT)
#==================================================================================
tops.configure(bg = 'black')
f1.configure(bg = 'black')
f2.configure(bg = 'black')

lb1info = Label(tops, text = 'CAFE MANAGEMENT SYSTEM', font = 'arial 16 bold', bd = 10, )
lb1info.pack()

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
#========================================================================================
def qExit():
    qExit = messagebox.askyesno("Quit system", "Do you want to quit ? ")
    if qExit > 0:
        root.destroy()
        return
def reset():
    paidtax.set("")
    subtotal.set("")
    total.set("")
    costofcakes.set("")
    costofdrinks.set("")
    servicecharge.set("")
    txtreciept.delete("1.0", END)

    e_latte.set('0')
    e_ice_tea.set('0')
    e_espresso.set('0')
    e_coffee.set('0')
    e_tea.set('0')
    e_ice_coffee.set('0')
    e_cappucino.set('0')
    e_iced_cappucino.set('0')

    e_red_cake.set('0')
    e_coffee_cake.set('0')
    e_black_forest_cake.set('0')
    e_boston_cream_cake.set('0')
    e_strawberry_cake.set('0')
    e_vanilla.set('0')
    e_choco_cake.set('0')
    e_choco_lava_cake.set('0')

#===================================================================================================================================

def costofitem():
    item1 = float(e_latta.get())
    item2 = float(e_espresso.get())
    item3 = float(e_tea.get())
    item4 = float(e_ice_tea.get())
    item5 = float(e_cappucino.get())
    item6 = float(e_iced_cappucino.get())
    item7 = float(e_coffee.get())
    item8 = float(e_ice_coffee.get())

    item9 = float(e_red_cake.get())
    item10 = float(e_coffee_cake.get())
    item11 = float(e_black_forest_cake.get())
    item12 = float(e_boston_cream_cake.get())
    item13 = float(e_vanilla.get())
    item14 = float(e_strawberry_cake.get())
    item15 = float(e_choco_cake.get())
    item16 = float(e_choco_lava_cake.get())

    priceofdrinks = (item1 * 2.5) + (item2 * 2.66) + (item3*3.05) + (item4 * 1.36) + (item5 * 1.88) + (item6 * 1.76) + (item7 * 2.154) + (item8 * 1.62)
    priceofcakess = (item9 * 3.5) + (item10 * 4.66) + (item11*5.05) + (item12 * 2.36) + (item13 * 6.88) + (item14 * 7.76) + (item15 * 8.154) + (item16 * 1.62)
    
    cakesprice = 

    costofcakes.set(cakesprice)
    costofdrinks.set(drinksprice)

#===================================================================================================================================
def chkbutton_value():
    if(var1.get() ==1 ):
        txtlatta.configure(state = NORMAL)
    elif var1.get() == 0:
        txtlatta.configure(state = DISABLED)
        e_latta.set("0")

    if(var2.get() ==1 ):
        txtespresso.configure(state = NORMAL)
    elif var2.get() == 0:
        txtespresso.configure(state = DISABLED)
        e_espresso.set("0")

    if(var3.get() ==1 ):
        txttea.configure(state = NORMAL)
    elif var3.get() == 0:
        txttea.configure(state = DISABLED)
        e_tea.set("0")

    if(var4.get() ==1 ):
        txtice_tea.configure(state = NORMAL)
    elif var4.get() == 0:
        txtice_tea.configure(state = DISABLED)
        e_ice_tea.set("0")

    if(var5.get() ==1 ):
        txtcappucino.configure(state = NORMAL)
    elif var5.get() == 0:
        txtcappucino.configure(state = DISABLED)
        e_cappucino.set("0")

    if(var6.get() ==1 ):
        txtice_cappucino.configure(state = NORMAL)
    elif var6.get() == 0:
        txtice_cappucino.configure(state = DISABLED)
        e_ice_cappucino.set("0")

    if(var7.get() ==1 ):
        txtcoffee.configure(state = NORMAL)
    elif var8.get() == 0:
        txtcoffee.configure(state = DISABLED)
        e_coffee.set("0")

    if(var8.get() ==1 ):
        txtice_coffee.configure(state = NORMAL)
    elif var8.get() == 0:
        txtice_coffee.configure(state = DISABLED)
        e_ice_coffee.set("0")

    if(var9.get() ==1 ):
        txtred_cake.configure(state = NORMAL)
    elif var9.get() == 0:
        txtred_cake.configure(state = DISABLED)
        e_red_cake.set("0")

    if(var10.get() ==1 ):
        txtcoffee_cake.configure(state = NORMAL)
    elif var10.get() == 0:
        txtcoffee_cake.configure(state = DISABLED)
        e_coffee_cake.set("0")

    if(var11.get() ==1 ):
        txtblack_forest_cake.configure(state = NORMAL)
    elif var11.get() == 0:
        txtblack_forest_cake.configure(state = DISABLED)
        e_black_forest_cake.set("0")

    if(var12.get() ==1 ):
        txtboston_cream_cake.configure(state = NORMAL)
    elif var12.get() == 0:
        txtboston_cream_cake.configure(state = DISABLED)
        e_boston_cream_cake.set("0")

    if(var13.get() ==1 ):
        txtvanilla_cake.configure(state = NORMAL)
    elif var13.get() == 0:
        txtvanilla_cake.configure(state = DISABLED)
        e_vanilla_cake.set("0")

    if(var14.get() ==1 ):
        txtstrawberry_cake.configure(state = NORMAL)
    elif var14.get() == 0:
        txtstrawberry_cake.configure(state = DISABLED)
        e_strawberry_cake.set("0")

    if(var15.get() ==1 ):
        txtchoco_cake.configure(state = NORMAL)
    elif var15.get() == 0:
        txtchoco_cake.configure(state = DISABLED)
        e_choco_cake.set("0")

    if(var16.get() ==1 ):
        txtchoco_lava_cake.configure(state = NORMAL)
    elif var16.get() == 0:
        txtchoco_lava_cake.configure(state = DISABLED)
        e_choco_lava_cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txtlatta.configure(state = DISABLED)
    txtespresso.configure(state = DISABLED)
    txttea.configure(state = DISABLED)
    txtice_tea.configure(state = DISABLED)
    txtcappucino.configure(state = DISABLED)
    txtice_cappucino.configure(state = DISABLED)
    txtcoffee.configure(state = DISABLED)
    txtice_coffee.configure(state = DISABLED)

    txtred_cake.configure(state = DISABLED)
    txtcoffee_cake.configure(state = DISABLED)
    txtblack_forest_cake.configure(state = DISABLED)
    txtboston_cream_cake.configure(state = DISABLED)
    txtvanilla_cake.configure(state = DISABLED)
    txtstrawberry_cake.configure(state = DISABLED)
    txtchoco_cake.configure(state = DISABLED)
    txtchoco_lava_cake.configure(state = DISABLED)


dateoforder = StringVar() 
reciept_ref = StringVar()
paidtax = StringVar()
subtotal = StringVar()
total = StringVar()
costofcakes = StringVar()
costofdrinks = StringVar()
servicecharge = StringVar()

#==============================================VARIABLES==========================================
e_latte = StringVar()
e_ice_tea = StringVar()
e_espresso = StringVar()
e_coffee  = StringVar()
e_tea = StringVar()
e_ice_coffee = StringVar()
e_cappucino = StringVar()
e_iced_cappucino = StringVar()

e_red_cake = StringVar()
e_coffee_cake = StringVar()
e_black_forest_cake = StringVar()
e_boston_cream_cake = StringVar()
e_strawberry_cake = StringVar()
e_vanilla = StringVar()
e_choco_cake = StringVar()
e_choco_lava_cake = StringVar()

dateoforder.set(time.strftime('%d/%m/%y'))

#=====================================================DRINKS======================================================

latta = Checkbutton(f1aa, text = 'LATTA \t', variable = var1, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 0, sticky = W)

ice_tea = Checkbutton(f1aa, text = 'ICE TEA \t', variable = var2, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 1, sticky = W)

espresso = Checkbutton(f1aa, text = 'ESPRESSO \t', variable = var3, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 2, sticky = W)

coffee = Checkbutton(f1aa, text = 'COFFEE \t', variable = var4, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 3, sticky = W)

tea = Checkbutton(f1aa, text = 'TEA \t', variable = var5, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 4, sticky = W)

ice_coffee = Checkbutton(f1aa, text = 'ICE COFFEE \t', variable = var6, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 5,sticky = W)

cappucino = Checkbutton(f1aa, text = 'CAPPUCINO \t', variable = var7, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 6, sticky = W)

iced_cappucino = Checkbutton(f1aa, text = 'ICED CAPPUCINO \t', variable = var8, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 7, sticky = W)

#=====================================================CAKES======================================================

red_cake = Checkbutton(f1ab, text = 'RED CAKE \t', variable = var9, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 0, sticky = W)

coffee_cake = Checkbutton(f1ab, text = 'COFFEE CAKE \t', variable = var10, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 1, sticky = W)

black_forest_cake = Checkbutton(f1ab, text = 'BLACK FOREST CAKE \t', variable = var11, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 2, sticky = W)

boston_cream_cake = Checkbutton(f1ab, text = 'BOSTON CREAM CAKE \t', variable = var12, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 3, sticky = W)

strawberry_cake = Checkbutton(f1ab, text = 'STRAWBERRY CAKE \t', variable = var13, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 4, sticky = W)

vanilla_cake = Checkbutton(f1ab, text = 'VANILLA CAKE \t', variable = var14, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 5, sticky = W)

choco_cake = Checkbutton(f1ab, text = 'CHOCO CAKE \t', variable = var15, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 6, sticky = W)

choco_lava_cake = Checkbutton(f1ab, text = 'CHOCO LAVA CAKE \t', variable = var16, onvalue = 1, offvalue = 0, font = 'arial 18 bold').grid(row = 7, sticky = W)

#=============================================ENTRY WIDGET FOR DRINKS=============================================

txtlatta = Entry(f1aa, font = 'arial 14 bold',textvariable = e_latte, bd = 6, width = 6, justify = 'left', state = DISABLED)
txtlatta.grid(row = 0, column = 1)

txtice_tea = Entry(f1aa, font = 'arial 14 bold',textvariable = e_tea, bd = 6, width = 6, justify = 'left', state = DISABLED)
txtice_tea.grid(row = 1, column = 1)

txtespresso = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_espresso, justify = 'left', state = DISABLED)
txtespresso.grid(row = 2, column = 1)

txtcoffee = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_coffee, justify = 'left', state = DISABLED)
txtcoffee.grid(row = 3, column = 1)

txttea = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_tea, justify = 'left', state = DISABLED)
txttea.grid(row = 4, column = 1)

txtice_coffee = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_ice_coffee, justify = 'left', state = DISABLED)
txtice_coffee.grid(row = 5, column = 1)

txtcappucino = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_cappucino, justify = 'left', state = DISABLED)
txtcappucino.grid(row = 6, column = 1)

txtice_cappucino = Entry(f1aa, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_iced_cappucino, justify = 'left', state = DISABLED)
txtice_cappucino.grid(row = 7, column = 1)


#=============================================ENTRY WIDGET FOR CAKES==============================================

txtred_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_red_cake, justify = 'left', state = DISABLED)
txtred_cake.grid(row = 0, column = 1)

txtcoffee_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_coffee_cake, justify = 'left', state = DISABLED)
txtcoffee_cake.grid(row = 1, column = 1)

txtblack_forest_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_black_forest_cake, justify = 'left', state = DISABLED)
txtblack_forest_cake.grid(row = 2, column = 1)

txtboston_cream_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_boston_cream_cake, justify = 'left', state = DISABLED)
txtboston_cream_cake.grid(row = 3, column = 1)

txtstrawberry_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_strawberry_cake, justify = 'left', state = DISABLED)
txtstrawberry_cake.grid(row = 4, column = 1)

txtvanilla_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6,textvariable = e_vanilla, justify = 'left', state = DISABLED)
txtvanilla_cake.grid(row = 5, column = 1)

txtchoco_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6, justify = 'left', state = DISABLED,textvariable = e_choco_cake)
txtchoco_cake.grid(row = 6, column = 1)

txtchoco_lava_cake = Entry(f1ab, font = 'arial 14 bold', bd = 6, width = 6, justify = 'left', state = DISABLED, textvariable = e_choco_lava_cake)
txtchoco_lava_cake.grid(row = 7, column = 1)

#============================================INFORMATION========================================================
lb1reciept = Label(ft2 , font = 'arial 14 bold', text = 'RECIEPT', bd = 2).grid(row = 0, column = 0, sticky = W)
txtreciept = Text(ft2, font = 'arial 14 bold', bd = 8, width = 40)
txtreciept.grid(row = 1, column = 0)

#============================================ITEM INFORMATION========================================================
lb1costofdrinks = Label(f2aa, font = 'arial 14 bold', text = 'COST OF DRINKS', bd = 8).grid(row=0, column = 0, sticky = W)
txtcostofdrinks = Entry(f2aa, font = 'arial 14 bold', bd = 8, justify = 'left',textvariable = costofdrinks).grid(row=0, column = 1, sticky = W)

lb1costofcakes = Label(f2aa, font = 'arial 14 bold', text = 'COST OF CAKES', bd = 8).grid(row=1, column = 0, sticky = W)
txtcostofcakes = Entry(f2aa, font = 'arial 14 bold', bd = 8, justify = 'left', textvariable = costofcakes).grid(row=1, column = 1, sticky = W)

lb1servicecharge = Label(f2aa, font = 'arial 14 bold', text = 'SERVICE CHARGE', bd = 8).grid(row=2, column = 0, sticky = W)
txtservicecharge = Entry(f2aa, font = 'arial 14 bold', bd = 8, justify = 'left',textvariable = servicecharge).grid(row=2, column = 1, sticky = W)

#============================================PAYMENT INFORMATION========================================================
lb1paidtax = Label(f2ab, font = 'arial 14 bold', text = 'TAX', bd = 8).grid(row=0, column = 0, sticky = W)
txtpaidtax = Entry(f2ab, font = 'arial 14 bold', bd = 8, justify = 'left', textvariable = paidtax).grid(row=0, column = 1, sticky = W)

lb1subtotal = Label(f2ab, font = 'arial 14 bold', text = 'SUB-TOTAL', bd = 8).grid(row=1, column = 0, sticky = W)
txtsubtotal = Entry(f2ab, font = 'arial 14 bold', bd = 8, justify = 'left', textvariable = subtotal).grid(row=1, column = 1, sticky = W)

lb1total = Label(f2ab, font = 'arial 14 bold', text = 'TOTAL', bd = 8).grid(row=2, column = 0, sticky = W)
txttotal = Entry(f2ab, font = 'arial 14 bold', bd = 8, justify = 'left', textvariable = total).grid(row=2, column = 1, sticky = W)

#==============================================BUTTON===========================================================
btnTotal = Button(fb2, text = 'TOTAL', fg = 'black', font = 'arial 10 bold', padx = 16, pady = 2, width = 5, bd = 4).grid(row = 0, column = 0)
btnReciept = Button(fb2, text = 'RECIEPT', fg = 'black', font = 'arial 10 bold', padx = 16, pady = 2, width = 5, bd = 4).grid(row = 0, column = 1)
btnReset = Button(fb2, text = 'RESET', fg = 'black', font = 'arial 10 bold',command = reset, padx = 16, pady = 2, width = 5, bd = 4).grid(row = 0, column = 2)
btnExit = Button(fb2, text = 'EXIT', fg = 'black', font = 'arial 10 bold',command = qExit, padx = 16, pady = 2, width = 5, bd = 4).grid(row = 0, column = 3)


root.mainloop()