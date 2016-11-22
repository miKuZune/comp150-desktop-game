def collide(yPos,floorObject):
    ReturnValue[0,False]
    if yPos >= floorObject:
        ReturnValue[0] = 1
        ReturnValue[1] = False
    else:
        ReturnValue[0] = 0
        ReturnValue[1] = True

    return ReturnValue

def outOfBounds(charXPos, limit):

    if charXPos >= limit:
        charXPos = limit
    elif charXPos <= 0:
        charXPos = 0

    return charXPos