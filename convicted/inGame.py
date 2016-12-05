import pygame
import floorCollision
import movement
import sys

pygame.init()

# Set screen size
WIDTH = 1700
HEIGHT = 800

#Direction of the character. For x 1 is right and -1 is left, 0 is no movement.
charXDirection = 0
charYDirection = 1
#Sets the starting position for the character.
charXpos = 75
charYPos = 0
#Sets the starting position for the floor.
floorXPos = 100
floorYPos = 900
#Used to check if the character has jumped and therefore if they are able to jump.
jumped = False

# Set up colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)
TRANSPARENT = (255,255,255,0)

counter = 0
counterIncrease = True

# Set up window
window = pygame.display.set_mode((WIDTH, HEIGHT),0, 32)

font = pygame.font.SysFont(None,48)
text = font.render("  ",True, WHITE,WHITE)
character = text.get_rect()
onFloor = False
isSliding = False

# Load images
characterImage = pygame.image.load('8bitDude.png')
skipImage = pygame.image.load('skipSmallSize.jpg')
binImage = pygame.image.load('binSmallSize.jpg')
characterImageSlide = pygame.image.load('8bitDudeSlide.jpg')
bikeRackImage = pygame.image.load('BikeRack.jpg')
wall = pygame.image.load('wall.png')
wall = pygame.transform.scale(wall,(30,100))

# Set image rect positions
firstFloor = (0, HEIGHT-20, WIDTH, 20)
building1 = (50,150,300,HEIGHT)
building1Roof = (50,150,300,20)
houseImage = (1300,680,400,600)
window1_1 = (80,200,40,40)
window1_2 = (160,700,40,40)
window1_3 = (80,600,40,40)
window1_4 = (160,500,40,40)
window1_5 = (80,400,40,40)
window1_6 = (160,300,40,40)
skip1 = (450,HEIGHT-77,132,57)
bin1 = (145,building1Roof[1] - 31,22,31)
bikeRack = (900,HEIGHT - 64,87,44)
wallObject = (320,building1Roof[1] - 100,30,100)

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
    if character.colliderect(firstFloor):
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
    onBin = character.colliderect(bin1)
    onSkip = character.colliderect(skip1)
    onBikeRack = character.colliderect(bikeRack)
    onWall = character.colliderect(wallObject)
    onBuilding = character.colliderect(building1Roof)
    onWindow1_1 = character.colliderect(window1_1)
    onWindow1_2 = character.colliderect(window1_2)
    onWindow1_3 = character.colliderect(window1_3)
    onWindow1_4 = character.colliderect(window1_4)
    onWindow1_5 = character.colliderect(window1_5)
    onWindow1_6 = character.colliderect(window1_6)
    #Position checkers to see if the player is at the boundry of the screen.
    charXpos = floorCollision.outOfBounds(charXpos,WIDTH)
    if onBuilding:
        onBuilding = False
        if charYPos >= building1Roof[1]-30:
            charYDirection = 0
            onFloor = True

    if onWindow1_1:
        onWindow1_1 = False
        if charYPos >= window1_1[1] +23:
            charYDirection = 0
            onFloor = True
    if onWindow1_2:
        onWindow1_2 = False
        if charYPos >= window1_2[1] + 23:
            charYDirection = 0
            onFloor = True
    if onWindow1_3:
        onWindow1_3 = False
        if charYPos >= window1_3[1]+23:
            charYDirection = 0
            onFloor = True
    if onWindow1_4:
        onWindow1_4 = False
        if charYPos >= window1_4[1]+23:
            charYDirection = 0
            onFloor = True
    if onWindow1_5:
        onWindow1_5 = False
        if charYPos >= window1_5[1]+23:
            charYDirection = 0
            onFloor = True
    if onWindow1_6 == True:
        onWindow1_6 = False
        if charYPos >= window1_6[1]+23:
            charYDirection = 0
            onFloor = True

    if onBin:
        onBin = False
        if charXpos >= bin1[0]+bin1[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= bin1[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= bin1[1]:
            charYDirection = 0
            onFloor = True
    if onSkip:
        onSkip = False
        if charXpos >= skip1[0] + skip1[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= skip1[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= skip1[1]:
            charYDirection = 0
            onFloor = True
    if onBikeRack:
        onBikeRack = False
        if charXpos >= bikeRack[0]+bikeRack[2] and isSliding == False:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= bikeRack[0] and isSliding == False:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= bikeRack[1]:
            charYDirection=0
            onFloor = True
    if onWall:
        onWall = False
        if charXpos >= wallObject[0] + wallObject[2]:
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                charXDirection = 1
            else:
                charXDirection = 0
        elif charXpos <= wallObject[0]:
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                charXDirection = -1
            else:
                charXDirection = 0
        elif charYPos <= wallObject[1]:
            charYDirection = 0
            onFloor = True


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
    pygame.draw.rect(window,GREY, firstFloor)
    pygame.draw.rect(window,GREY,building1)
    pygame.draw.rect(window,WHITE,window1_1)
    pygame.draw.rect(window,WHITE,window1_2)
    pygame.draw.rect(window,WHITE,window1_3)
    pygame.draw.rect(window,WHITE,window1_4)
    pygame.draw.rect(window,WHITE,window1_5)
    pygame.draw.rect(window,WHITE,window1_6)

    window.blit(binImage,(bin1[0],bin1[1]))
    window.blit(skipImage,(skip1[0],skip1[1]))
    window.blit(bikeRackImage,(bikeRack[0],bikeRack[1]))
    window.blit(wall,(wallObject[0],wallObject[1]))


    if isSliding:
        window.blit(characterImageSlide,(charXpos - 9,charYPos - 6))
        charSlidingRect = (charXpos,charYPos,40,20)
        charXDirection = movement.slide(charXDirection)
        if charXDirection > 0:
            charXDirection -= 0.1
        elif charXDirection < 0:
            charXDirection += 0.1
    elif counterIncrease == True:
        window.blit(characterImage,(charXpos - 10,charYPos - 23))


    clock = pygame.time.Clock()
    clock.tick(500)
    pygame.display.update()