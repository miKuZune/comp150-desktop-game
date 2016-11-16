def moveLeft(xDirection):
    if xDirection >= -2.5:
        xDirection -= 0.1
    else:
        xDirection = -3.5

    return xDirection

def moveRight(xDirection):
    if xDirection <= 3.5:
        xDirection += 0.1
    else:
        xDirection = 3.5

    return xDirection

def jump(yPos):
    yDirection = -4
    yPos -= 1

    return yDirection,yPos

def slide(xDirection):
    if xDirection > 0:
        xDirection = 4
    elif xDirection < 0:
        xDirection = -4
    else:
        xDirection = 0

    return xDirection