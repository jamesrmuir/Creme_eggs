#Import modules================================================================#
import pygame, sys

#Imports some useful constants
from pygame.locals import *

#Initialise the pygame module
pygame.init()

#Sets the display
displayWindow = pygame.display.set_mode((300,300))

#Gives the window a title
pygame.display.set_caption("Tile test")

#Loop forever
while True:
    #Gets all user events
    for event in pygame.event.get():
        #If the user wants to quit
        if event.type == QUIT:
            #Ends the game
            pygame.quit()
            sys.exit()

    #Draws green square
    pygame.draw.rect(displayWindow, (0,255,0), (100,50,20,20))
    
    #Updates the display
    pygame.display.update()
