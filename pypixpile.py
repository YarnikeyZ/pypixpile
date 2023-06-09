ESC = "\033"
CCLR = f"{ESC}[0;0m"
CLR = f"{CCLR}{ESC}[H{ESC}[2J{ESC}[3J"

def colorIt(text='', colorIdFg=0, colorIdBg=0):
    """Colors text"""
    return f'{ESC}[38;5;{colorIdFg}m{ESC}[48;5;{colorIdBg}m{text}{CCLR}'

def colorThem(colorIdFg=0, colorIdBg=0):
    """Colors terminal post it's output"""
    return f'{ESC}[38;5;{colorIdFg}m{ESC}[48;5;{colorIdBg}m'

def moveCursor(posX=0, posY=0):
    """Moves cursor to (posX, posY)"""
    return f"{ESC}[{posY};{posX}H"

def checkCollision(rect1, rect2, colltype):
    """Checks collisions with the edge of other obj.

    rect1 = [posX[0], posY[1], sizeX[2], sizeY[3], speedX[4], speedY[5]]
    
    rect2 = [posX[0], posY[1], sizeX[2], sizeY[3], speedX[4], speedY[5]]
    """
    
    coll = False
    if colltype == 0:
        if rect1[0] + rect1[2] >= rect2[0] + rect2[2]:
            rect1[4] = -rect1[4]
            rect1[0] -= rect1[2]
            coll = True
        elif rect1[0] <= rect2[0]:
            rect1[4] = -rect1[4]
            rect1[0] = rect2[0]
            coll = True
        if rect1[1] + rect1[3] >= rect2[1] + rect2[3]:
            rect1[5] = -rect1[5]
            rect1[1] -= rect1[3]
            coll = True
        elif rect1[1] <= rect2[1]:
            rect1[5] = -rect1[5]
            rect1[1] = rect2[1]
            coll = True
    elif colltype == 1:
        if rect1[0] + rect1[2] + rect1[4] > rect2[0] and rect1[0] + rect1[4] < rect2[0] + rect2[2] and rect1[1] + rect1[3] > rect2[1] and rect1[1] < rect2[1] + rect2[3]:
            rect1[4] = -rect1[4]
            coll = True
        if rect1[0] + rect1[2] > rect2[0] and rect1[0] < rect2[0] + rect2[2] and rect1[1] + rect1[3] + rect1[5] > rect2[1] and rect1[1] + rect1[5] < rect2[1] + rect2[3]:
            rect1[5] = -rect1[5]
            coll = True
    elif colltype == 2:
        if rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0] and rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]:
            coll = True
    
    return rect1[0], rect1[1], rect1[2], rect1[3], rect1[4], rect1[5], coll

def drawPixel(sym='', colorIdFg=0, colorIdBg=0, posX=0, posY=0):
    """Draws a pixel on a canvas"""
    print(f"{moveCursor(posX, posY)}{colorIt(sym, colorIdFg, colorIdBg)}")

def drawRectangle(sym='', colorIdFg=0, colorIdBg=0, posX=0, posY=0, geomX=0, geomY=0, fill=True):
    """Draws a rectangle on a canvas"""
    line = sym*(geomX)
    print(f"{moveCursor(posX, posY)}{colorThem(colorIdFg, colorIdBg)}{line if not fill else ''}", end="")
    for geomPosY in range(0, geomY+1):
        print(f"{moveCursor(posX, posY+geomPosY)}{line if fill else sym+moveCursor(posX+geomX, posY+geomPosY)+sym}", end="")
    print(f"{moveCursor(posX, posY+geomY)}{line}", end="")
    

def drawEllipse(sym='', colorIdFg=0, colorIdBg=0, posX=0, posY=0, radX=0, radY=0, fill=True):
    """Draws a ellipse on a canvas"""
    x = 0
    y = radY
    d1 = radY**2 - radX**2 * radY + 0.25 * radX**2
    dx = x * 2 * radY**2
    dy = y * 2 * radX**2

    if fill:
        for fillY in range(-radY, radY):
            for fillX in range(-radX, radX):
                if fillX*fillX*radY*radY+fillY*fillY*radX*radX <= radY*radY*radX*radX:
                    drawPixel(sym, colorIdFg, colorIdBg, int(posX + fillX), int(posY + fillY))

    while dx < dy:
        drawPixel(sym, colorIdFg, colorIdBg, x+posX, y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, -x+posX, y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, x+posX, -y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, -x+posX, -y+posY)
        if d1 < 0:
            x += 1
            dx += 2 * radY**2
            d1 += dx + radY**2
        else:
            x += 1
            y -= 1
            dx += 2 * radY**2
            dy -= 2 * radX**2
            d1 += dx - dy + radY**2
    d2 = (radY**2 * (x + 0.5)**2) + \
        (radX**2 * (y - 1)**2) - (radX**2 * radY**2)
    for y in range(y, -1, -1):
        drawPixel(sym, colorIdFg, colorIdBg, x+posX, y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, -x+posX, y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, x+posX, -y+posY)
        drawPixel(sym, colorIdFg, colorIdBg, -x+posX, -y+posY)
        if d2 > 0:
            dy -= 2 * radX**2
            d2 += radX**2 - dy
        else:
            x += 1
            dx += 2 * radY**2
            dy -= 2 * radX**2
            d2 += dx - dy + radX**2

def drawLine(sym='', colorIdFg=0, colorIdBg=0, x0=0, y0=0, x1=0, y1=0):
    """Draws a line on a canvas"""
    steep = abs(y1 - y0) > abs(x1 - x0)

    if steep:
        temp = x0
        x0 = y0
        y0 = temp
        temp = x1
        x1 = y0
        y0 = temp

    if x0 > x1:
        temp = x0
        x0 = y0
        y0 = temp
        temp = x1
        x1 = y0
        y0 = temp

    dX = x1 - x0
    dY = abs(y1 - y0)
    steepY = 1 if y0 < y1 else -1
    y = y0
    error = dX / 2

    for x in range(x0, x1):
        drawPixel(sym, colorIdFg, colorIdBg, y if steep else x, x if steep else y)
        error -= dY
        if error < 0:
            y += steepY
            error += dX
