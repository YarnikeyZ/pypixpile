ESC = "\033"
CLR = f"{ESC}[0;0m{ESC}[H{ESC}[2J{ESC}[3J"

def colorIt(text, colorIdText, colorIdBackground):
    """Colors text"""
    return f'{ESC}[38;5;{colorIdText}m{ESC}[48;5;{colorIdBackground}m{text}{ESC}[0;0m'

def moveCursor(posX, posY):
    """Moves cursor to (posX, posY)"""
    return f"{ESC}[{posY};{posX}H"

def checkCollision(rect1: list, rect2: int, colltype: int):
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

def drawPixel(sym: str, colorIdFg: int, colorIdBg: int, posX: int, posY: int):
    """Draws a pixel on a canvas"""
    return f"{ESC}[38;5;{colorIdFg}m{ESC}[48;5;{colorIdBg}m{ESC}[{posY+1};{posX+1}H{sym}"

def drawRectangle(sym: str, colorIdFg: int, colorIdBg: int, posX: int, posY: int, geomX: int, geomY: int):
    """Draws a rectangle on a canvas"""
    line = sym*geomX
    rect = f"{ESC}[38;5;{colorIdFg}m{ESC}[48;5;{colorIdBg}m"
    for g_y in range(geomY):
        rect += f"{ESC}[{posY+1+g_y};{posX+1}H{line}"
    return rect

def drawEllipse(sym: str, colorIdFg: int, colorIdBg: int, posX: int, posY: int, radX: int, radY: int):
    """Draws a ellipse on a canvas"""
    x = 0
    y = radY
    d1 = radY**2 - radX**2 * radY + 0.25 * radX**2
    dx = x * 2 * radY**2
    dy = y * 2 * radX**2
    while dx < dy:
        print(drawPixel(sym, colorIdFg, colorIdBg, x+posX, y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, -x+posX, y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, x+posX, -y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, -x+posX, -y+posY))
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
        print(drawPixel(sym, colorIdFg, colorIdBg, x+posX, y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, -x+posX, y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, x+posX, -y+posY))
        print(drawPixel(sym, colorIdFg, colorIdBg, -x+posX, -y+posY))
        if d2 > 0:
            dy -= 2 * radX**2
            d2 += radX**2 - dy
        else:
            x += 1
            dx += 2 * radY**2
            dy -= 2 * radX**2
            d2 += dx - dy + radX**2

def drawLine(sym: str, colorIdFg: int, colorIdBg: int, x0: int, y0: int, x1: int, y1: int):
    """Draws a line on a canvas"""
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        length = abs(dx)
    else:
        length = abs(dy)
    ddx = dx / length
    ddy = dy / length
    x = x0
    y = y0
    print(drawPixel(sym, colorIdFg, colorIdBg, round(x), round(y)))
    for i in range(length):
        x += ddx
        y += ddy
        print(drawPixel(sym, colorIdFg, colorIdBg, round(x), round(y)))
