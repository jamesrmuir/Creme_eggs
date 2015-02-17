#Imports modules
import pygame
import time

#Initalises pygame
pygame.init()

#Sets display width and height
display_width = 800
display_height = 600

#Defines colour
black = (  0,  0,  0)
white = (255,255,255)
red =   (255,  0,  0)

#Defines car 
car_width = 73

#Set's the display
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Sets the game's title
pygame.display.set_caption('A bit Racey')

#Set's clock rate
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load('Images/racecar.png')

#Car function
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#Text thing
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
    
    
#Calls the message_display 
def crash():
    message_display('You Crashed')

#Main game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Keboard input start
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            #Keboard input end

        #Changes car location
        x += x_change

        #Sets background to white
        gameDisplay.fill(white)

        #Calls car function
        car(x,y)

        #Checks if user is of the screen if they are it displays a message
        if x > display_width - car_width or x < 0:
            crash()
            
        #Updates the display and sets rate of which it does that
        pygame.display.update()
        clock.tick(60)

#Calls the game loop
game_loop()

#Quits the game
pygame.quit()
quit()
