import pygame, sys
from pygame.locals import *

# Set up pygame
pygame.init()

# Set up colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)

# Set up window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Convicted')

# Check if player has jumped
jumped = False

# Set up road
road = (0, 880, WINDOW_WIDTH, 40)

# Set up player
character = pygame.sprite.Sprite()
character.image = pygame.image.load('runningman.png').convert_alpha()
character.image = pygame.transform.scale(character.image, (150, 150))
character.rect = character.image.get_rect()
character.rect.x = 0
character.rect.y = 740

# Set up wall
wall = pygame.sprite.Sprite()
wall.image = pygame.image.load('concretewall.png')
wall.image = pygame.transform.scale(wall.image, (138, 273))
wall.rect = wall.image.get_rect()
wall.rect.x = 860
wall.rect.y = 610

# Set up bin
bin = pygame.sprite.Sprite()
bin.image = pygame.image.load('bin_192px.png')
bin.rect = bin.image.get_rect()
bin.rect.x = 250
bin.rect.y = 730

# Set up bike rack
bikeRack = pygame.sprite.Sprite()
bikeRack.image = pygame.image.load('BikeRack.png')
bikeRack.image = pygame.transform.scale(bikeRack.image, (400, 400))
bikeRack.rect = bikeRack.image.get_rect()
bikeRack.rect.x = 450
bikeRack.rect.y = 610

#run game loop
while True:

    pressed = pygame.key.get_pressed()

    # keep player on screen
    if character.rect.x < 0:
        character.rect.x = 0
    if character.rect.x > 1050:
        character.rect.x = 1050
    if character.rect.y < 0:
        character.rect.y = 0
    if character.rect.y > 1050:
        character.rect.y = 1050

    # Set up keyboard controls for movement
    dist = 5
    if pressed[pygame.K_LEFT]:
        character.rect.x -= dist
    if pressed[pygame.K_RIGHT]:
        character.rect.x += dist
    if pressed[pygame.K_SPACE] and jumped == False:
        character.rect.y += -50
        jumped = True

    onBin = character.rect.colliderect(bin.rect)
    if character.rect.colliderect(bin.rect) == True:
        onBin = True
    else:
        onBin = False

    hitWall = character.rect.colliderect(wall.rect)
    if character.rect.colliderect(wall.rect) == True:
        hitWall = True
    else:
        hitWall = False

    hitBike = character.rect.colliderect(bikeRack.rect)
    if character.rect.colliderect(bikeRack.rect) == True:
        hitBike = True
    else:
        hitBike = False

    if onBin == True:
        onBin = False
        if character.rect.x >= bin.rect:
            if pressed[K_RIGHT] or pressed[K_d]:
                character.rect.x = 1
            else:
                character.rect.x = 1
        elif character.rect.x <= bin.rect:
            if pressed[K_LEFT] or pressed[K_a]:
                character.rect.x = 1
            else:
                character.rect.x = 160
        elif character.rect.y <= bin.rect:
            character.rect.y = 0
            if pressed[K_SPACE]:
                character.rect.y = -4

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pressed[K_ESCAPE]:
        pygame.quit()
        sys.exit()

    window.fill(WHITE)
    pygame.draw.rect(window, GREY, road)
    window.blit(character.image, character.rect)
    window.blit(wall.image, wall.rect)
    window.blit(bin.image, bin.rect)
    window.blit(bikeRack.image, bikeRack.rect)
    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.update()