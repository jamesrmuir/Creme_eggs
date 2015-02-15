#Imports modules
from tkinter import *
import subprocess

#Function to launch files
def buttonOne():
    subprocess.call("pyGameKeyInputTest.py", shell=True)
def buttonTwo():
    subprocess.call("pyGameTestFileTwo.py", shell=True)

mainWindow = Tk()

buttonOne = Button(mainWindow, text="1", command=buttonOne)
buttonOne.grid(row=0, column=0)
buttonTwo = Button(mainWindow, text="2", command=buttonTwo)
buttonTwo.grid(row=0, column=1)

