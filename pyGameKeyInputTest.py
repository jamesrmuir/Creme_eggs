#Imports pygame module
import pygame

#Initalizes pygame
pygame.init()

#Defines game display width and height
display_width = 800
display_height = 600

#Sets up display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("pyGame keyboard test")

#Defines colours
black = (  0,  0,  0)
white = (255,255,255)

#Sets up clock rate
clock = pygame.time.Clock()

#Defines variables
crashed = False
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

#Loads assets
carImg = pygame.image.load("Images/raceCarPlacer.png")

#Car Function
def car(x, y):
    gameDisplay.blit(carImg, (x,y))

#Main game lop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #Key Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################
    ##
    x += x_change
    ##         
    gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()









    
