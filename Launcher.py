#Metadata======================================================================#
__author__ = "James"
#Import========================================================================#
from tkinter import *
import commonVariables

#Functions=====================================================================#
def mainMenu():
    #Title
    title = Label(mainWindow, text="Main Menu")
    title.grid(row=0, column=0)

    #Changes the resolution
    changeResolution = Button(mainWindow, text="Change Resolution", command=resolutionMenu)
    changeResolution.grid(row=1, column=0)
    
def resolutionMenu():
    #Title
    title = Label(mainWindow, text="Change resolution")
    title.grid(row=0, column=0)

    back = Button(mainWindow, text="Back", command=mainMenu)
    back.grid(row=1, column=0)
    
    
#Program=======================================================================#
#Sets TK window
mainWindow = Tk()

mainMenu()
