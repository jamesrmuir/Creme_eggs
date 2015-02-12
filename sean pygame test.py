import pygame
pygame.init()
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Creme Egg Project")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

