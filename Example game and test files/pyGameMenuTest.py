#Imports modules
import pygame
import time
import random

#Initalises pygame
pygame.init()

#Sets the height and width of the display
display_width = 800
display_height = 600

#Defines colours
black        = (  0,  0,  0)
white        = (255,255,255)
red          = (255,  0,  0)
block_colour = ( 53,115,255)

#Sets the width of the car
car_width = 73

#Sets up the display and its title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Menu Test")

#Sets up the clock
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load("Images/racecar.png")

#Displays amount of images dodged
def things_dodged(count):
    font = pygame.font.SusFont(None,25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#Things
def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])

#Function thats used to create the car
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#Text objects
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Message display
def message_display(text):
    largeText = pygame.font.Font("fresansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    #Updates display
    pygame.display.update()

    #Sleeps for two seconds
    time.sleep(2)

    #Calls game loop
    game_loop()

#Displays crashed message
def crash():
    message_display("You crashed")

#Game intro
def game_intro():
    #Declares intro
    intro = True

    #While loop
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white) #Sets background white
        largeText = pygame.font.Font("freesansbold.ttf", 115) #Sets a font
        TextSurf, TextRect = text_objects("Menu Test", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

#Main game loop
def game_loop():
    x = (display_width * 0.45)  
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Checks for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.type == pygame.K_RIGHT:
                    x_change = 5

            #Checks for key releases
            if event.type == pygame.KEYUP:
                if event.key == pygame.L_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Changes x
        x += x_change

        #Sets display to white
        gameDisplay.fill(white)

        #Calls things and passes things to it
        things(thing_startx, thing_starty, thing_width, thing_height, block_colour)            

        thing_starty += thing_speed

        #Calls car and things_dodged
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        #Updates the display
        pygame.display.update()
        clock.tick(60)
            
#Calls game
game_intro()
game_loop()

#Quits the game
pygame.quit()
quit()
            





































