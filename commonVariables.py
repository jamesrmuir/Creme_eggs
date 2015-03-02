import pickle

#Default
def default():
    global displayWidth, displayHeight, graphicsBarOne
    displayWidth = 800
    displayHeight = 600 
    graphicsBarOne = 0

    save()
#Saves the game
def save():
    global displayWidth, displayHeight, graphicsBarOne
    
    with open("savegame.txt", "wb") as f:
        pickle.dump(displayWidth, f)
        pickle.dump(displayHeight, f)
        pickle.dump(graphicsBarOne, f)
    
#Loads the game
def load():
    global displayWidth, displayHeight, graphicsBarOne

    with open("savegame.txt", "rb") as f:
        displayWidth = pickle.load(f)
        displayHeight = pickle.load(f)
        graphicsBarOne = pickle.load(f)

default()

with open("savegame.txt", "rb") as f:
    var1 = pickle.load(f)
    var2 = pickle.load(f)
    var3 = pickle.load(f)

displayWidth = var1
displayHeight = var2
graphicsBarOne = var3
