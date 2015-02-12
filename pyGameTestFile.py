#pyGame test
__author__ = "James Muir"
__version__ = "1.0"

#Imports modules
import pygame

#Initialises pygame
pygame.init() 

#Defines screen
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("A creme eggs test game")

#Set's clock rate
clock = pygame.time.Clock()


#Main game loop
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        print(event)

    pygame.display.update()
    clock.tick(60) #Sets FPS

#Quits the game
pygame.quit()
quit()



    
