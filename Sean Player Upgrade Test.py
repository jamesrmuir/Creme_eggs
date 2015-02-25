from tkinter import *

points = 100
points=int(points)


def pace():
    if points==0:
        lab2 = Label(mainWindow, text="You have no points to spend")
        lab2.pack()

    else:
        #starting the pace and attack variables with 10
        pace = 10
        pace=int(pace)
        pace = pace + 10
      
        


        lab3 = Label(mainWindow, text="The pace of your character is now level")
        lab3.pack()
        lab4 = Label(mainWindow, text=pace)
        lab4.pack()
        

    

mainWindow = Tk()

mainWindow.title("Upgrade Menu")
mainWindow.minsize(width=500,height=500)

lab1 = Label(mainWindow, text="Upgrade your character here!")
lab1.pack()

but1 = Button(mainWindow, text="Click here to upgrade the pace of your player",command=pace)
but1.pack()
