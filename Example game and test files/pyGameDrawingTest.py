#Imports modules
import pygame
import time
import random

#Initalise pygame
pygame.init()

#Sets the size of the display
display_width = 800
display_height = 600

#Define colours
black = (  0,  0,  0)
white = (255,255,255)
red   = (255,  0,  0)

#Sets the width of the car
car_width = 73

#Sets display
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Sets game title
pygame.display.set_caption("Object drawing test")

#Clock rate
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load("Images/racecar.png")

#Function to draw square
def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy,thingw, thingh])

#Car
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Displays message
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#Calls the message display function and passes "You Crashed" to it
def crash():
    message_display('You Crashed')

#Start of the game function
def game_loop():
    #Defines x and y should be out of the loop
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

#Start of the object being drawn
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
#End of the object being drawn

    #Game exit variable
    gameExit = False

    #Start of game loop
    while not gameExit:

        #Start of checking for key presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        #End of checking for key presses

        #Changes x
        x += x_change

        #Sets the display white
        gameDisplay.fill(white)

     
        #Calls functions 
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)

        #Checks if the player has left the screen and if so displays message
        if x > display_width - car_width or x < 0:
            crash()

        #
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            
        #Refeshes the display
        pygame.display.update()
        clock.tick(60)

#Calls game loop
game_loop()

#Quits the game
pygame.quit()
quit()
