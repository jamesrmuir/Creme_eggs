#Import modules================================================================#
import pygame, sys

#Imports some useful constants
from pygame.locals import *

#Defines resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

#Defines colours
BLACK = (  0,  0,  0)
BROWN = (153, 76,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

#Links resources and colours
colours  = {
            DIRT  : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            COAL  : BLACK
           }

#List representing out tilemap
tilemap = [
            [GRASS, COAL,  DIRT ],
            [WATER, WATER, GRASS],
            [COAL,  GRASS, WATER],
            [DIRT,  GRASS, COAL ],
            [GRASS, WATER, DIRT ]
          ]

#Defines game dimensions
TILESIZE = 40
MAPWIDTH = 3
MAPHEIGHT = 5

#Initialise the pygame module
pygame.init()

#Sets the display
displayWindow = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#Gives the window a title
pygame.display.set_caption("Tile") 

#Loop forever
while True:
    #Gets all user events
    for event in pygame.event.get():
        #If the user wants to quit
        if event.type == QUIT:
            #Ends the game
            pygame.quit()
            sys.exit()

    #Loop through each row        
    for row in range(MAPHEIGHT):
        #Loop through each column
        for column in range(MAPWIDTH):
            #Draws tiles 
            pygame.draw.rect(displayWindow, colours[tilemap[row][column]],(column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
    
    #Updates the display
    pygame.display.update()
