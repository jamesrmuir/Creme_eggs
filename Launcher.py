#Metadata======================================================================#
__author__ = "James"
#Import========================================================================#
import commonVariables
import pygame

#Variables=====================================================================#
black        = (  0,  0,  0)
white        = (255,255,255)
red          = (200,  0,  0)
green        = (  0,200,  0)
brightRed   = (255,  0,  0)
brightGreen = (0  ,255,  0)
grey         = (135,139,140)
yellow       = (198,217, 30)
brightYellow = (233,255, 36)

#Functions=====================================================================#
def textObjectsYellow(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def textObjectsGrey(text, font):
    textSurface = font.render(text, True, grey)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()

def button(msg,x,y,w,h,ic,ac,action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    
    #smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
def menu():
    
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
        
        #Displays menu
        TextSurf, TextRect = textObjectsYellow("Menu", largeText)

        
        TextRect.center = ((commonVariables.displayWidth/2),(commonVariables.displayHeight/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        #Gets mouse position
        mouse = pygame.mouse.get_pos()

        #print(mouse)

        #Button One
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, brightYellow,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, yellow,(150,450,100,50))

        #Button One Text
        textSurf, textRect = textObjectsGrey("Resolution", smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)

        #Button Two
        if 350+100 > mouse[0] > 350 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, brightYellow,(350,450,100,50)) #surface colour (left, top, width, height)
        else:
            pygame.draw.rect(gameDisplay, yellow,(350,450,100,50))

        #Button Two Text
        textSurf, textRect = textObjectsGrey("Gamemode", smallText)
        textRect.center = ( (350+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        
        #Button Three    
        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450: 
            pygame.draw.rect(gameDisplay, brightYellow,(550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, yellow,(550,450,100,50))
        
        #Button Three Text
        textSurf, textRect = textObjectsGrey("Sound", smallText)
        textRect.center = ( (550+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)        
        
        #Update display
        pygame.display.update()
        clock.tick(15)
    
#Program=======================================================================#
#Initalise pygame
pygame.init()

gameDisplay = pygame.display.set_mode((commonVariables.displayWidth
                                       ,commonVariables.displayHeight))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

#Calls variable
menu()
