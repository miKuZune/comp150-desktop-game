import pygame
import floorCollision
import movement
import sys

pygame.init()

# Set screen size
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500

# Set colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
TRANSPARENT = (255,255,255,0)

# Set up window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT),0, 32)

# Direction of the character. For x 1 is right and -1 is left, 0 is no movement.
charXDirection = 0
charYDirection = 1
# Sets the starting position for the character.
charXpos = 50
charYPos = 0
# Set floor position
floorXPos = 100
floorYPos = 900

# Set counter
counter = 0
counterIncrease = True

# Set character states
jumped = False
onFloor = False
isSliding = False

# Set up character
character = pygame.sprite.Sprite()
character.image = pygame.image.load('8bitDude.png')
character.image2 = pygame.image.load('8bitDude.jpg')
character.rect = character.image.get_rect()

# Set up character slide
characterslide = pygame.sprite.Sprite()
characterslide.imageSlide = pygame.image.load('8bitDudeSlide.jpg')
characterslide.rect = characterslide.imageSlide.get_rect()

# Set up floor
firstFloor = (0, WINDOW_HEIGHT - 20, WINDOW_WIDTH, 20)

# Set up wall
wall = pygame.sprite.Sprite()
wall.image = pygame.image.load('wall.png')
wall.image = pygame.transform.scale(wall.image, (30, 100))
wall.rect = wall.image.get_rect()
wall.rect.x = 700
wall.rect.y = WINDOW_HEIGHT - 120

# Set up bin
bin = pygame.sprite.Sprite()
bin.image = pygame.image.load('binSmallSize.jpg')
bin.rect = bin.image.get_rect()
bin.rect.x = 300
bin.rect.y = WINDOW_HEIGHT - 51

# Set up skip
skip = pygame.sprite.Sprite()
skip.image = pygame.image.load('skipSmallSize.jpg')
skip.rect = skip.image.get_rect()
skip.rect.x = 450
skip.rect.y = WINDOW_HEIGHT - 77

# Set up bike rack
bikeRack= pygame.sprite.Sprite()
bikeRack.image = pygame.image.load('BikeRack.jpg')
bikeRack.rect = bikeRack.image.get_rect()
bikeRack.rect.x = 900
bikeRack.rect.y = WINDOW_HEIGHT - 64

# Set up game loop
while True:
                                                                                                                        #Checks if the player is pressing any key. Listener.
    pressed = pygame.key.get_pressed()
    charYDirection += 0.1

    if pressed[pygame.K_SPACE] and onFloor:
        jumped = True
        charYDirection, charYPos = movement.jump(charYPos)
    elif pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        isSliding = True
    else:
        isSliding = False

    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        charXDirection = movement.moveLeft(charXDirection)
    elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        charXDirection = movement.moveRight(charXDirection)
    else:
        charXDirection = 0


                                                                                                                        #Checks if the players position is less than the position of the floor. If it is then it brings the player back up one space.
    if character.rect.colliderect(firstFloor):
        if charYPos >= firstFloor[1]+20:
            charYDirection = 1
        else:
            onFloor = True
    else:
        onFloor = False

    if onFloor == True:
        charYDirection = 0
        jumped = False
                                                                                                                        #Checks if the player is pressing the right or d arrow keys. If they are the character moves to the right.
    # Set up character collision
    onBin = character.rect.colliderect(bin.rect)
    onSkip = character.rect.colliderect(skip.rect)
    onBikeRack = character.rect.colliderect(bikeRack.rect)
    onWall = character.rect.colliderect(wall.rect)

    if character.rect.colliderect(bin.rect):
        onBin = True
    elif character.rect.colliderect(skip.rect):
        onSkip = True
    elif character.rect.colliderect(bikeRack.rect):
        onBikeRack = True
    elif character.rect.colliderect(wall.rect):
        onWall = True
    else:
        onBin = False
        onSkip = False
        onBikeRack = False


    # Keep character on screen
    charXpos = floorCollision.outOfBounds(charXpos,WINDOW_WIDTH)

    if onBin:
        onBin = False
        if charXpos >= bin.rect[0]+bin.rect[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= bin.rect[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= bin.rect[1]:
            charYDirection = 0
        if pressed[pygame.K_SPACE]:
            charYDirection = -4
    if onSkip == True:
        onSkip = False
        if charXpos >= skip.rect[0] + skip.rect[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= skip.rect[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= skip.rect[1]:
            charYDirection = 0
            if pressed[pygame.K_SPACE]:
                charYDirection = -4
    if onBikeRack == True:
        onBikeRack = False
        if charXpos >= bikeRack.rect[0]+bikeRack.rect[2] and isSliding:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= bikeRack.rect[0] and isSliding:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= bikeRack.rect[1]:
            charYDirection=0
            if pressed[pygame.K_SPACE]:
                charYDirection = -4
    if onWall == True:
        onWall = False
        if charXpos >= wall.rect[0] + wall.rect[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= wall.rect[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= wall.rect[1]:
            charYDirection = 0
            if pressed[pygame.K_SPACE]:
                charYDirection = -4


    charXpos = charXpos + charXDirection
    charYPos = charYPos + charYDirection
    character.centerx = charXpos
    character.centery = charYPos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    window.fill(WHITE)


    window.blit(character.image, character.rect)
    if isSliding == True:
        window.blit(characterslide.rect, (charXpos - 9, charYPos - 6))
        #charSlidingRect = (charXpos,charYPos,40,20)
        charXDirection = movement.slide(charXDirection)
        if charXDirection > 0:
            charXDirection -= 0.1
        elif charXDirection < 0 :
            charXDirection += 0.1


    elif counterIncrease == True:
        pygame.draw.rect(window, WHITE, character)
        counter +=1
        window.blit(character.image, (charXpos - 10, charYPos - 23))
        if(counter >= 25):
            counterIncrease = False
    else:
        pygame.draw.rect(window, WHITE, character)
        counter-=1
        window.blit(character.image2,(charXpos - 10, charYPos - 23))
        if(counter <=0):
            counterIncrease = True


    pygame.draw.rect(window, GREY, firstFloor)
    window.blit(bin.image,(bin.rect[0],bin.rect[1]))
    window.blit(skip.image,(skip.rect[0],skip.rect[1]))
    window.blit(bikeRack.image,(bikeRack.rect[0],bikeRack.rect[1]))
    window.blit(wall.image,(wall.rect[0],wall.rect[1]))

    clock = pygame.time.Clock()
    clock.tick(300)
    pygame.display.update()