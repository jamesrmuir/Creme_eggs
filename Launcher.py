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

        #Defines text
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = textObjects("Menu", largeText)
        TextRect.center = ((commonVariables.displayWidth/2),(commonVariables.displayHeight/2))
        gameDisplay.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        #print(mouse)

        #Button One
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, brightYellow,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, yellow,(150,450,100,50))

        #Button Two    
        pygame.draw.rect(gameDisplay, yellow,(550,450,100,50))
        pygame.display.update()
        clock.tick(15)

def textObjects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    game_loop()
    
#Program=======================================================================#
#Initalise pygame
pygame.init()

gameDisplay = pygame.display.set_mode((commonVariables.displayWidth
                                       ,commonVariables.displayHeight))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()

#Calls variable
menu()
