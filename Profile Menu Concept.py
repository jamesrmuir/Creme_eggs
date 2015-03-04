from tkinter import *

mainWindow = Tk()
mainWindow.title("Pi Thon Profile Menu")
mainWindow.minsize(width=400,height=400)
mainWindow.config(bg = "light green")

def userNamePopUp():
    userName = ent1.get()
    messagebox.showinfo(title="Username changed",message="Your new username is "+userName)



lab1 = Label(mainWindow, text="Create a new username:", fg = "blue", bg = "light green", font=('times',30, 'bold'))
lab1.pack()

ent1 = Entry(mainWindow, fg = "green", bg = "light green", font=('times',20, 'bold'))
ent1.pack()

but1 = Button(mainWindow,text="Confirm", fg = "light green", bg = "green", command=userNamePopUp, font=('times',15, 'bold'))
but1.pack()

mainloop()
