import pygame
pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creme Egg Project")
font = pygame.font.SysFont('Calibri', 25, True, False)


clock = pygame.time.Clock()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

screen.fill(WHITE)
pygame.display.flip()

text = font.render("The Creme Egg Project",True,BLACK)
screen.blit(text, [25, 50])
pygame.display.flip()



done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()



