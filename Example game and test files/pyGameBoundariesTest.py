#Imports pygame module
import pygame

#Sets display width and height
display_width = 800
display_height = 600

#Defines colours
black = (  0,  0,  0)
white = (255,255,255)
red   = (255,  0,  0)

#Defines car width
car_width = 73

#Sets the display up
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Sets the title of the game
pygame.display.set_caption("Boundry test")

#Sets up the clock
clock = pygame.time.Clock()

#Loads assets
carImg = pygame.image.load("Images/racecar.png")

#Car function
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #If key pressed down    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            #If key released 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Changes the location of the car
        x += x_change

        #Sets the background
        gameDisplay.fill(white)

        #Calls car function
        car(x,y)

        #Stops car going of screen
        if x > display_width - car_width or x < 0:
            gameExit = True

        #Sets the display update and update rate
        pygame.display.update()
        clock.tick(60)

#Calls the game loop
game_loop()
pygame.quit()
quit()
        
        
























        
