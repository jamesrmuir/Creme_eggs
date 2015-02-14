#pyGame test
__author__ = "James Muir"
__version__ = "1.1"

#Imports modules
import pygame

#Variables
crashed = False
display_width = 800
display_height = 600
x = (display_width * 0.45) #Used for car width
y = (display_height * 0.8) #Used for car height

#Initialises pygame
pygame.init() 

#Defines screen
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A creme eggs test game")

#Defines colours in order to make them more recon
black = (  0,   0, 0  )
white = (255, 255, 255)

#Set's clock rate
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load("Images/raceCarPlacer.png")

#Car function
def car(x, y):
    gameDisplay.blit(carImg, (x,y))   

#Main game loop
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    gameDisplay.fill(white) #Sets background
    car(x,y) #Sets up car

    pygame.display.update()
    clock.tick(60) #Sets FPS



#Quits the game
pygame.quit()
quit()



    
