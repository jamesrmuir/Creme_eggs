#Metadata======================================================================#
__author__ = "James"
#Import========================================================================#
from tkinter import *
import commonVariables

#Functions=====================================================================#
def main():
    #Sets TK window
    mainWindow = Tk()

    #Title
    title = Label(mainWindow, text="Main Menu")
    title.grid(row=0, column=0)

    #Changes the resolution
    changeResolution = Button(mainWindow, text="Change Resolution")

#Program=======================================================================#
main()
