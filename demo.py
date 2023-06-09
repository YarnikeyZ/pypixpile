from os import get_terminal_size as gts
from time import sleep as sl
from pypixpile.pypixpile import *

def render(fps: int):
    canvas = list(gts())
    canvas = (canvas[0]-1, canvas[1])
    """Renders an "image" to the screen."""
    try:
        while True:
            drawRectangle("@", 117, 0, 0, 0, canvas[0], canvas[1])
            drawRectangle("g", 40 , 0, 0, canvas[1]-7 , canvas[0], 7)
            drawRectangle("h", 208, 0, canvas[0]-23, canvas[1]-13, 21, 10)
            drawRectangle("d", 9, 0, canvas[0]-21, canvas[1]-9 , 5, 6)
            drawRectangle("w", 11, 0, canvas[0]-14, canvas[1]-10, 10, 5)
            drawRectangle("f", 208, 0, canvas[0]-10, canvas[1]-10, 2, 5)
            drawRectangle("f", 208, 0, canvas[0]-14, canvas[1]-8 , 10, 1)
            drawRectangle("h", 11, 0, canvas[0]-18, canvas[1]-7 , 1, 1) 
            drawLine("r", 9, 0, canvas[0]-24, canvas[1]-13, canvas[0]-11, canvas[1]-19)
            drawLine("r", 9, 0, canvas[0]-13, canvas[1]-19, canvas[0], canvas[1]-12)
            drawLine("r", 9, 0, canvas[0]-24, canvas[1]-13, canvas[0], canvas[1]-13)
            drawLine("r", 9, 0, canvas[0]-21, canvas[1]-14, canvas[0]-2, canvas[1]-14)
            drawLine("r", 9, 0, canvas[0]-19, canvas[1]-15, canvas[0]-4, canvas[1]-15)
            drawLine("r", 9, 0, canvas[0]-17, canvas[1]-16, canvas[0]-6, canvas[1]-16)
            drawLine("r", 9, 0, canvas[0]-15, canvas[1]-17, canvas[0]-8, canvas[1]-17)
            drawEllipse("s", 11, 0, 16, 7, 10, 5)
            drawEllipse("l", 21, 0, 20, canvas[1]-4, 15, 2)
            sl(1/fps)
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(CLR, end="")
    render(1)
    # print(CLR, end="")

if __name__ == "__main__":
    main()
