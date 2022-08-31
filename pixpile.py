def check_collision(pos: int, size: int, speed: int, canvas: int):
    """Checks collisions with the edge of other obj."""
    pos += speed
    if pos + size >= canvas:
        speed = -speed
        pos = canvas - size
        return pos, speed, True
    elif pos <= 0:
        speed = -speed
        pos = 0
        return pos, speed, True
    return pos, speed, False

def draw_pixel(sym: str, color_id: int, posx: int, posy: int):
    """Draws a pixel on a canvas"""
    print(f"\033[38;5;{color_id}m\033[{posy+1};{posx+1}H{sym}")

def draw_rectangle(sym: str, color_id: int, posx: int, posy: int, geomx: int, geomy: int):
    """Draws a rectangle on a canvas"""
    line = sym*geomx
    print(f"\033[38;5;{color_id}m", end="")
    for g_y in range(geomy):
        print(f"\033[{posy+1+g_y};{posx+1}H{line}")

def draw_ellipse(sym: str, color_id: int, posx: int, posy: int, radx: int, rady: int):
    """Draws a ellipse on a canvas"""
    x = 0
    y = rady
    d1 = rady**2 - radx**2 * rady + 0.25 * radx**2
    dx = x * 2 * rady**2
    dy = y * 2 * radx**2
    while dx < dy:
        draw_pixel(sym, color_id, x+posx, y+posy)
        draw_pixel(sym, color_id, -x+posx, y+posy)
        draw_pixel(sym, color_id, x+posx, -y+posy)
        draw_pixel(sym, color_id, -x+posx, -y+posy)
        if d1 < 0:
            x += 1
            dx += 2 * rady**2
            d1 += dx + rady**2
        else:
            x += 1
            y -= 1
            dx += 2 * rady**2
            dy -= 2 * radx**2
            d1 += dx - dy + rady**2
    d2 = (rady**2 * (x + 0.5)**2) + (radx**2 * (y - 1)**2) - (radx**2 * rady**2)
    for y in range(y, -1, -1):
        draw_pixel(sym, color_id, x+posx, y+posy)
        draw_pixel(sym, color_id, -x+posx, y+posy)
        draw_pixel(sym, color_id, x+posx, -y+posy)
        draw_pixel(sym, color_id, -x+posx, -y+posy)
        if d2 > 0:
            dy -= 2 * radx**2
            d2 += radx**2 - dy
        else:
            x += 1
            dx += 2 * rady**2
            dy -= 2 * radx**2
            d2 += dx - dy + radx**2

def draw_line(sym: str, color_id: int, x0: int, y0: int, x1: int, y1: int):
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
    draw_pixel(sym, color_id, round(x), round(y))
    for i in range(length):
        x += ddx
        y += ddy
        draw_pixel(sym, color_id, round(x), round(y))
