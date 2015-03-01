def default():
    file = open("saveGame.txt", "w")

    #Width
    file.write("800")
    file.write("\n")
    #Height
    file.write("600")
    file.write("\n")
    #Graphics setting bar one
    file.write("400")
    file.write("\n")

    file.close()

def load():
    global displayWidth, displayHeight, graphicsBarOne
    
    #Sets the height and width
    with open("saveGame.txt") as f:
        fileContent = f.readlines()
            
    displayWidth = int(fileContent[0])
    displayHeight = int(fileContent[1])
    graphicsBarOne = int(fileContent[2])


