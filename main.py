from pygame import *
from keys import create_keys, draw_keys
from settings import *
from sounds import *
init()

screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("forte-Piano")

keys = create_keys(len(KEYS))

pressed_keys = set()
sounds = load_sounds(KEYS)
keys_list = list(KEYS.keys())

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(keys):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)
        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(keys):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)

        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()        
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)    
                

    screen.fill(WHITE)
    draw_keys(screen, keys, pressed_keys)
    display.update()

