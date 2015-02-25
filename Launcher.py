#Imports modules=================================================================================================#
import pygame

#Functions=======================================================================================================#

#Declaring variables=============================================================================================#
#Sets variable 
display_width = 800
display_height  = 600

#Defines colours
black = (  0,  0,  0)
white = (255,255,255)

#Main program====================================================================================================#
#Initalise pygame
pygame.init()

#Sets up the display and its title
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Sets clock
clock = pygame.time.Clock()

