import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (190,0,0)
green = (0,200,0)
cyan = (19,229,240)
purple = (151,19,240)
orange = (224,143,2)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_cyan = (19,200,240)
bright_purple = (182,107,232)
bright_orange = (235,193,122)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Project Creme Egg')
clock = pygame.time.Clock()

def quitgame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    
    if x+w > mouse[0] > x and y+50 > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Project Creme Egg", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)

        button("Singleplayer",325,200,150,50,green,bright_green,)
        button("Multiplayer",325,275,150,50,purple,bright_purple,)
        button("Options",325,350,150,50,cyan,bright_cyan,)
        button("Quit",325,425,150,50,red,bright_red,quitgame)
        button("<",75,312,150,50,orange,bright_orange,)
        button(">",575,312,150,50,orange,bright_orange,)
        
        pygame.display.update()
        clock.tick(15)

game_intro()
