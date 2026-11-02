from pygame import *
from settings import *

init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("forte-Piano")

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    screen.fill(WHITE)
    display.update()
    


    screen.fill(WHITE)
    display.update()

