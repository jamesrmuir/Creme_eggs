#Imports modules
import pygame
import time
import random

#Initalise pygame
pygame.init()

#Sets the displays width and height
display_width = 800
display_height = 600

#Defines colours
black        = (  0,  0,  0)
white        = (255,255,255)
red          = (255,  0,  0)
block_colour = ( 53,115,255)

#Car width
car_width = 73

#Sets up the display and  title
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Score test")

#Set's up the clock
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load("Images/racecar.png")

#Displays how many things have been dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

#Thing
def things(thingx, thingy, thingw, thingh, colour):
    pygame.draw.rect(gameDisplay, colour, [thingx, thingy, thingw, thingh])

#Displays car
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#Text object
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Displays message
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    #Updates the display
    pygame.display.update()
    
    #Sleeps for two seconds
    time.sleep(2)

    #Calls game_loop()
    game_loop()

#Calls message display and passes "You crashed" to it
def crash():
    message_display("You Crashed")

#Start of game loop
def game_loop():
    #Sets x and y which are used for the car
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #Sets variables
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    #Variable that tracks how many items have been dodged
    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            #Allows the player to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            #Checks for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            #Check for key release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Changes the position of x
        x += x_change

        #Sets the display to white
        gameDisplay.fill(white)

        #Calls things and passes a bunch of things to it
        things(thing_startx, thing_starty, thing_width, thing_height, block_colour)

        
        #Modifies variables
        thing_starty += thing_speed

        #Calls functions
        car(x,y)
        things_dodged(dodged)
            
        #Checks if the player has left the screen and calls crash() if it has
        if x > display_width - car_width or x < 0:
            crash()

        #Each times a block is re-generated it adds one to the dodged counts 
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            
        #Print when the y location of the car crosses the box
        if y < thing_starty + thing_height:
            print("y crossover")
            #Print when the x location of the car crosses the box
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()
                
        #Updates display
        pygame.display.update()
        clock.tick(60)

#Calls the game loop
game_loop()

#Quits the game
pygame.quit()
quit()



































