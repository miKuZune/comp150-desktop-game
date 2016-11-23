import pygame, sys
import os
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# Set up background
background = pygame.image.load('Menu Design 1.5-1.png')
background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))

# Blit window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.blit(background, (0, 0))

# Load icon
icon = pygame.image.load('8bitDude.jpg')
pygame.display.set_icon(icon)

# Blit menu to screen
pygame.display.set_caption('Start Screen')
pygame.display.update()

running = True
while running:
    mousePos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == True:
        import inGame.py
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
quit()