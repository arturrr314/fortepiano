from pygame import *
from keys import create_keys, draw_keys
from settings import *

init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("forte-Piano")

keys = create_keys(len(KEYS))

pressed_keys = set()



while True:
    for e in event.get():
        if e.type == QUIT:
            quit()



    screen.fill(WHITE)
    draw_keys(screen, keys, pressed_keys)
    display.update()

