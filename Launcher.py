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
bright_red   = (255,  0,  0)
bright_green = (0  ,255,  0)

#Functions=====================================================================#
def menu():
    
    intro = True

    while intro:
        #Allows the player to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #Sets screen to white
        gameDisplay.fill(white)

        #Defines text
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = textObjects("Menu", largeText)
        TextRect.center = ((commonVariables.displayWidth/2),(commonVariables.displayHeight/2))
        gameDisplay.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        pygame.display.update()
        clock.tick(15)

def textObjects(text, font):
    textSurface = font.render(text, True, black)
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
