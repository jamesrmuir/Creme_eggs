#Metadata======================================================================#
__author__ = "James"
#Imports modules===============================================================#
import commonVariables
import pygame
import socket

#Variables=====================================================================#
#Defines colour
black        = (  0,  0,  0)
white        = (255,255,255)
red          = (200,  0,  0)
green        = (  0,200,  0)
brightRed    = (255,  0,  0)
brightGreen  = (0  ,255,  0)
grey         = (135,139,140)
yellow       = (198,217, 30)
brightYellow = (233,255, 36)

#Defines user Ip
userIp = socket.gethostbyname(socket.gethostname())

#Defines variable for the loop in mainMenu
menuLoop = True
#Functions=====================================================================#
#Creates yellow text-----------------------------------------------------------#
def textObjectsYellow(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

#Creates grey text-------------------------------------------------------------#
def textObjectsGrey(text, font):
    textSurface = font.render(text, True, grey)
    return textSurface, textSurface.get_rect()

#Button function that creates buttons------------------------------------------#
def button(msg,x,y,w,h,ic,ac,textObjects,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",22)    
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#Used to test things and as a placer-------------------------------------------#
def testFunction():
    print("Test")

#The main menu-----------------------------------------------------------------#
def mainMenu():
    global menuLoop
    
    menuLoop = False
    menuLoop = True

    while menuLoop:
        #Allows the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Sets screen to white
        gameDisplay.fill(grey)

        #Defines text sizes
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        smallText = pygame.font.Font("freesansbold.ttf",  20)
        
        #Displays title
        TextSurf, TextRect = textObjectsYellow("Project Pithon", largeText)
        TextRect.center = ((commonVariables.displayWidth/2),(commonVariables.displayHeight/5))
        gameDisplay.blit(TextSurf, TextRect)
        
        #Gets mouse position
        mouse = pygame.mouse.get_pos()

        #Button One
        button("Gamemode",150,450,100,50,yellow,brightYellow,textObjectsGrey,gamemode)
        
        #Button Two
        button("Graphics",350,450,100,50,yellow,brightYellow,textObjectsGrey,graphics)
        
        #Button Three    
        button("Sound",550,450,100,50,yellow,brightYellow,textObjectsGrey,sound)

        #IP Display
        button(userIp,700,550,100,50,grey,grey,textObjectsYellow,testFunction)

        #Version display
        button("V0.5 Pre Alpha",5,550,100,50,grey,grey,textObjectsYellow,testFunction)       
        
        #Update display
        pygame.display.update()
        clock.tick(15)

#Called when button one (gamemode) is pressed----------------------------------#
def gamemode():
    global menuLoop
    
    menuLoop = False
    menuLoop = True
    
    while menuLoop:
        #Allows the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Sets screen to white
        gameDisplay.fill(grey)

        #Defines text sizes
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        mediumText = pygame.font.Font("freesansbold.ttf", 50)
        smallText = pygame.font.Font("freesansbold.ttf",  20)
        
        #Displays title
        TextSurf, TextRect = textObjectsYellow("Graphics menu", mediumText)
        TextRect.center = ((400),(85)) 
        gameDisplay.blit(TextSurf, TextRect)
        
        #Gets mouse position
        mouse = pygame.mouse.get_pos()

        #Minus button
        button("-",50,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Percentage display
        button("",200,263,commonVariables.graphicsBarOne,25,yellow,yellow,textObjectsGrey,testFunction)        

        #Plus button
        button("+",650,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Button One
        #button("Gamemode",150,450,100,50,yellow,brightYellow,textObjectsGrey,gamemode)
        
        #Button Two (Back)
        button("Back",350,450,100,50,yellow,brightYellow,textObjectsGrey,mainMenu)
        
        #Button Three    
        #button("Sound",550,450,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
  
        #IP Display
        button(userIp,700,550,100,50,grey,grey,textObjectsYellow,testFunction)

        #Version display
        button("V0.5 Pre Alpha",5,550,100,50,grey,grey,textObjectsYellow,testFunction)       
        
        #Update display
        pygame.display.update()
        clock.tick(15)
        
#Called when button two (Resolution) is pressed--------------------------------#
def graphics():
    global menuLoop
    
    menuLoop = False
    menuLoop = True
    
    while menuLoop:
        #Allows the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Sets screen to white
        gameDisplay.fill(grey)

        #Defines text sizes
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        mediumText = pygame.font.Font("freesansbold.ttf", 50)
        smallText = pygame.font.Font("freesansbold.ttf",  20)
        
        #Displays title
        TextSurf, TextRect = textObjectsYellow("Graphics menu", mediumText)
        TextRect.center = ((400),(85)) 
        gameDisplay.blit(TextSurf, TextRect)
        
        #Gets mouse position
        mouse = pygame.mouse.get_pos()

        #Minus button
        button("-",50,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Percentage display
        button("",200,263,commonVariables.graphicsBarOne,25,yellow,yellow,textObjectsGrey,testFunction)        

        #Plus button
        button("+",650,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Button One
        #button("Gamemode",150,450,100,50,yellow,brightYellow,textObjectsGrey,gamemode)
        
        #Button Two (Back)
        button("Back",350,450,100,50,yellow,brightYellow,textObjectsGrey,mainMenu)
        
        #Button Three    
        #button("Sound",550,450,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
  
        #IP Display
        button(userIp,700,550,100,50,grey,grey,textObjectsYellow,testFunction)

        #Version display
        button("V0.5 Pre Alpha",5,550,100,50,grey,grey,textObjectsYellow,testFunction)       
        
        #Update display
        pygame.display.update()
        clock.tick(15)
        
#Sound-------------------------------------------------------------------------#
def sound():
    global menuLoop
    
    menuLoop = False
    menuLoop = True
    
    while menuLoop:
        #Allows the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Sets screen to white
        gameDisplay.fill(grey)

        #Defines text sizes
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        mediumText = pygame.font.Font("freesansbold.ttf", 50)
        smallText = pygame.font.Font("freesansbold.ttf",  20)
        
        #Displays title
        TextSurf, TextRect = textObjectsYellow("Graphics menu", mediumText)
        TextRect.center = ((400),(85)) 
        gameDisplay.blit(TextSurf, TextRect)
        
        #Gets mouse position
        mouse = pygame.mouse.get_pos()

        #Minus button
        button("-",50,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Percentage display
        button("",200,263,400,25,yellow,yellow,textObjectsGrey,testFunction)        

        #Plus button
        button("+",650,250,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
        
        #Button One
        #button("Gamemode",150,450,100,50,yellow,brightYellow,textObjectsGrey,gamemode)
        
        #Button Two (Back)
        button("Back",350,450,100,50,yellow,brightYellow,textObjectsGrey,mainMenu)
        
        #Button Three    
        #button("Sound",550,450,100,50,yellow,brightYellow,textObjectsGrey,testFunction)
  
        #IP Display
        button(userIp,700,550,100,50,grey,grey,textObjectsYellow,testFunction)

        #Version display
        button("V0.5 Pre Alpha",5,550,100,50,grey,grey,textObjectsYellow,testFunction)       
        
        #Update display
        pygame.display.update()
        clock.tick(15)
    

#Program=======================================================================#
#Loads variables---------------------------------------------------------------#
commonVariables.load()

#Initalise pygame--------------------------------------------------------------#
pygame.init()

gameDisplay = pygame.display.set_mode((commonVariables.displayWidth
                                       ,commonVariables.displayHeight))
pygame.display.set_caption("Launcher")
clock = pygame.time.Clock()

#Launches the program----------------------------------------------------------#
mainMenu()






















