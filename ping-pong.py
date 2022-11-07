from pygame import *

window_width, window_height = 800, 600

window = display.set_mode((window_width, window_height))

display.set_caption("Ping-Pong Oyunu")

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()