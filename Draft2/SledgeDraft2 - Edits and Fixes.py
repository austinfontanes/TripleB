'''
Program: Sledge Inventory App
Developer: Triple B Consulting
Date: April 17, 2021
Purpose: The application assists Sledge employees with inventory tracking.
'''
#imports necessary GUI tools
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

#Defines tools to be used
myGUI=Tk()
myGUI.geometry('1350x750+0+0')
myGUI.title('Sledge Inventory App') #creates app title

#formats the top frame
TopFrame = Frame(myGUI, width = 1350, height = 100, bd=14, relief='raise')
TopFrame.pack(side=TOP)

#formats the bottom frame
BottomFrame = Frame(myGUI, width = 1350, height = 100, bd=14, relief='raise')
BottomFrame.pack(side=BOTTOM)

#formats the left frame
LeftMidFrame = Frame(BottomFrame, width = 600, height = 1000, bd =14, relief ='raise')
LeftMidFrame.pack(side=LEFT)

#formats the right frame
RightMidFrame = Frame(BottomFrame, width = 750, height = 1000, bd =14, relief ='raise')
RightMidFrame.pack(side=RIGHT)

#page title
lblTitle = Label(TopFrame, font = ('roboto', 40, 'bold'), text="REPORT INVENTORY", bd =10, width=41, justify='center')
lblTitle.grid(row=0,column=0)

#product name / item description
lblDubsSpirit = Label(RightMidFrame, font=('roboto',36,'bold'), text = "DUBS SPIRIT 500mL", bd = 0, width = 20, relief='flat')
lblDubsSpirit.grid(row=0,column=0)

#entry label
lblCount = Label(RightMidFrame, font=('roboto',30,'bold'), text = "Bottle Count:", bd = 0, width = 20)
lblCount.grid(row=1,column=0)

#entry box
countEntry = Entry(RightMidFrame, font=('roboto',25,'bold'), text = "Next Item", width = 10, bd = 5)
countEntry.grid(row=1,column=1)

#next button
nextBut = Button(RightMidFrame, font=('roboto',25,'bold'), text = "Next Item", width = 20)
nextBut.grid(row=8,column=0)

#previous button 
prevBut = Button(RightMidFrame, font=('roboto',25,'bold'), text = "Previous Item", width = 20)
prevBut.grid(row=10,column=0)

#item picture
dubsPic = Image.open('s746342102120056129_p117_i4_w640.png')
dubsPicResize = dubsPic.thumbnail((300, 300))
itemCanvas = Canvas(LeftMidFrame, width = 300, height = 300)      
itemCanvas.pack()      
img = PhotoImage(file="image_300.png")
itemCanvas.create_image(20,20, anchor=NW, image=img)
itemCanvas.grid(row=0,column=0)

#logo picture
load= Image.open("sledge-distillery-2017-final-logo-12-1-17.png")
render = ImageTk.PhotoImage(load)
logo = Label(TopFrame, image=render)
logo.grid(row=0,column=1)

#exit button
exitBut = Button(RightMidFrame, font=('roboto',20,'bold'), text = "Exit to Main Menu", width = 20)
exitBut.grid(row=10,column=5)

myGUI.mainloop()
