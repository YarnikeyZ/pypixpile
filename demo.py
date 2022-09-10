from os import get_terminal_size as gts
from time import sleep as sl
from pixpile import *

clr = "\033[0;0m\033[H\033[2J\033[3J"

def render(fps: int):
    canvas = list(gts())
    canvas[1] += -1
    """Renders an "image" to the screen."""
    try:
        while True:
            print(draw_rectangle("@", 117, 0, 0, canvas[0], canvas[1]))
            print(draw_rectangle("g", 40, 0, canvas[1]-3, canvas[0], 7))
            print(draw_rectangle("h", 208, canvas[0]-23, canvas[1]-13, 21, 10))
            print(draw_rectangle("d", 9, canvas[0]-21, canvas[1]-9, 5, 6))
            print(draw_rectangle("w", 11, canvas[0]-14, canvas[1]-10, 10, 5))
            print(draw_rectangle("f", 208, canvas[0]-10, canvas[1]-10, 2, 5))
            print(draw_rectangle("f", 208, canvas[0]-14, canvas[1]-8, 10, 1))
            print(draw_rectangle("h", 11, canvas[0]-18, canvas[1]-7, 1, 2))
            draw_ellipse("s", 11, 16, 7, 10, 5)
            draw_ellipse("s", 11, 16, 7, 9, 5)
            draw_ellipse("s", 11, 16, 7, 8, 5)
            print(draw_rectangle("s", 11, 9, 3, 15, 9))
            draw_ellipse("l", 21, 20, canvas[1]-4, 15, 2)
            print(draw_rectangle("l", 21, 6, canvas[1]-5, 29, 3))
            draw_line("r", 9, canvas[0]-24, canvas[1]-12, canvas[0]-13, canvas[1]-18)
            draw_line("r", 9, canvas[0]-13, canvas[1]-18, canvas[0]-2, canvas[1]-12)
            draw_line("r", 9, canvas[0]-24, canvas[1]-12, canvas[0]-2, canvas[1]-12)
            draw_line("r", 9, canvas[0]-21, canvas[1]-13, canvas[0]-5, canvas[1]-13)
            draw_line("r", 9, canvas[0]-19, canvas[1]-14, canvas[0]-7, canvas[1]-14)
            draw_line("r", 9, canvas[0]-17, canvas[1]-15, canvas[0]-9, canvas[1]-15)
            draw_line("r", 9, canvas[0]-15, canvas[1]-16, canvas[0]-11, canvas[1]-16)
            print(draw_pixel("r", 9, canvas[0]-13, canvas[1]-17))
            sl(1/fps)
            canvas = list(gts())
            canvas[1] += -1
    except KeyboardInterrupt:
        return

def main():
    """A function responsible for initialization"""
    print(clr, end="")
    render(10)
    print(clr, end="")

if __name__ == "__main__":
    main()
