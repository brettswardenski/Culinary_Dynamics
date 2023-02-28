'''
Author: Brett Swardenski 
Assignment: SDEV 140 Final Project
Description: 
'''

from tkinter import *
from menu import *

root = Tk()
root.title('Culinary Dynamics')
root.geometry('800x720')
root.resizable(False, False)


def mainScreen():
    welcome.destroy()
    start.destroy()

    topFrame.config(height=100)
    title.config(font=('Helvetica', 24))

    global leftFrame
    leftFrame = Frame(root, bg="orange", height=520, width=(800/3))
    leftFrame.grid(row=1, column=0, sticky=W)

    global middleFrame
    middleFrame = Frame(root, bg="red", height=520, width=(800/3))
    middleFrame.grid(row=1, column=1, sticky=W)

    global rightFrame
    rightFrame = Frame(root, bg="grey", height=520, width=(800/3))
    rightFrame.grid(row=1, column=2, sticky=W)
'''
    for x in menuCategories:
        button = Button(rightFrame, text=x, font=('Helvetica', 18), \
                    width=6, height=1)
        button.pack(side=TOP, pady=5)

    bottomFrame.config(height=100)
'''



def startScreen():
    topFrame.config(height=360)
    bottomFrame.config(height=360)

    title.config(font=('Helvetica', 48))
    global start
    start = Button(bottomFrame, text='Start', font=('Helvetica', 18), \
                    width=8, height=3, command=mainScreen)
    start.place(anchor=CENTER, relx=0.5, rely=0.15)
    global welcome
    welcome = Label(topFrame, text='Welcome!', font=('Helvetica', 28))
    welcome.place(anchor=CENTER, relx=0.5, rely=0.75)
    

topFrame = Frame(root, bg="green", width=800)
topFrame.grid(row=0, column=0, columnspan=3)

title = Label(topFrame, text='Culinary Dynamics')
title.place(anchor=CENTER, relx=0.5, rely=0.5)

bottomFrame = Frame(root, bg="blue", width=800)
bottomFrame.grid(row=2, column=0, columnspan=3, sticky=N)

startScreen()




root.mainloop()