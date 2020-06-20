from tkinter import *

root  = Tk()
root.geometry("780x633")
root.maxsize(1280,980)
root.minsize(480,360)
root.title("Ankit GUI ")

#Important label options
#text - adds try:
#bd - background
#fd - foreground
#font - sets font
#1      font=("comicsansms",15, "bold")    tuple method
#2      font="comicsansms 15 bold"          string method
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RIDGE, RAISED, GROOVE

title_label = Label(text = '''Selena Marie Gomez (born July 22, 1992) is an American singer, songwriter, actress, and television producer.[1] 
\nAfter appearing on the children's television series Barney & Friends (2002–2004),
\n she received wider recognition for her portrayal of Alex Russo on the Emmy 
\nAward-winning Disney Channel television series Wizards of Waverly Place, 
\nwhich aired from 2007 until 2012. Gomez also starred in the films Another Cinderella Story (2008),
\n Princess Protection Program (2009), Wizards of Waverly Place: The Movie (2009), Ramona and Beezus (2010),
\n, and Monte Carlo (2011). Thereafter, she focused on more mature roles in Spring Breakers (2012), Getaway (2013),
\n The Fundamentals of Caring (2016), and The Dead Don't Die (2019). She voices the character of Mavis in the
 \n Hotel Transylvania film franchise, and serves as an executive producer of the Netflix television drama series
  \n13 Reasons Why (2017–present) and the Netflix documentary series Living Undocumented (2019).''', 
  bg = "red",
   fg = "blue",
    padx = 95,
     pady=94,
      font="fantasy 8 bold",
       borderwidth = 3,
        relief = RIDGE)

#important pack options
#anchor to move the content based on north east west south.
#side = top, bottom, left, right

#title_label.pack(side = BOTTOM, anchor = "nw", fill = Y, padx = 36, pady = 94)
title_label.pack(side = TOP,  fill = X)

root.mainloop()