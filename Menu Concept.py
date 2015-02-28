from tkinter import *

def Start():
    messagebox.showinfo(title="Creme Eggs Game",message="The game will now launch...")

def Profile():
    messagebox.showinfo(title="Creme Eggs Profile Settings",message="The Profile Options menu will now launch...")

def Settings():
    messagebox.showinfo(title="Creme Eggs Settings",message="The settings menu will now launch...")

def Quit():
    quit()

    



mainWindow = Tk()
mainWindow.title("Creme Eggs Menu")
mainWindow.minsize(width=800,height=600)

menuTitle = Label(mainWindow, text="Creme Eggs Game Menu", font=('arial',40, 'bold'))
menuTitle.pack()

butStart = Button(mainWindow, text="Start",command=Start, height=5, width=50)
butStart.pack()

butProfile = Button(mainWindow, text="Profile Options",command=Profile, height=5, width=50)
butProfile.pack()

butSettings = Button(mainWindow, text="Settings Menu",command=Settings, height=5, width=50)
butSettings.pack()

butQuit = Button(mainWindow, text="Quit",command=Quit, height=5, width=50)
butQuit.pack()


