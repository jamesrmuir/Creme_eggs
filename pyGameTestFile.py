#pyGame test
__author__ = "James Muir"
__version__ = "1.0"

#Imports modules
import pygame

#Variables
crashed = False

#Initializes pyGame
pygame.init() 

#Set's up the display
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

#Set's the clock
clock = pygame.time.Clock()

#Main game loop
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()



    
