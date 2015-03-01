from tkinter import *  #---Imports tkinter for use---#
import socket #---Imports the socket function for finding the IP---#


#---Finds User IP---#
playerIp = socket.gethostbyname(socket.gethostname())

#---Defines the button commands and launches a message box where, in the final game, the program would be imported and run. On the quit command, it quits the menu---#

def Start():
    messagebox.showinfo(title="Pi Thon Game",message="The game will now launch...")

def Profile():
    messagebox.showinfo(title="Pi Thon Profile Settings",message="The Profile Options menu will now launch...")

def Settings():
    messagebox.showinfo(title="Pi Thon Settings",message="The settings menu will now launch...")

def New():
    messagebox.showinfo(title="Pi Thon New Features",message="Added the New Features section, added user IP to the Launcher, added version number to the Launcher.")

def Quit():
    quit()

    

#---Launches the windows and sets the size to 800x600---#

mainWindow = Tk()
mainWindow.title("Pi Thon Menu")
mainWindow.minsize(width=800,height=600)

#---Creates title--#

menuTitle = Label(mainWindow, text="Pi Thon Game Menu", font=('arial',40, 'bold'))
menuTitle.pack()

ipLabel = Label(mainWindow, text=playerIp, font=('arial',10, 'bold'))
ipLabel.pack()

versionLabel = Label(mainWindow,text="Launcher 0.3 Concept", font=('arial',10, 'bold'))
versionLabel.pack()

#---Creates buttons---#

butStart = Button(mainWindow, text="Start",command=Start, height=5, width=50)
butStart.pack()

butProfile = Button(mainWindow, text="Profile Options",command=Profile, height=5, width=50)
butProfile.pack()

butSettings = Button(mainWindow, text="Settings Menu",command=Settings, height=5, width=50)
butSettings.pack()

butNew = Button(mainWindow, text="What's new?",command=New, height=5, width=50)
butNew.pack()

butQuit = Button(mainWindow, text="Quit",command=Quit, height=5, width=50)
butQuit.pack()


