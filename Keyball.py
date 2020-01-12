# Simple moving dot use x / o keys to affect movement

import pew


pew.init()                  # intialise device
screen = pew.Pix()          # create empty screen image

x = 3                       # intial x position
y = 1                       # intial y position
dx = 1                      # initial x step
dy = 1                      # initial y step

while True:
    keys = pew.keys()
    screen.pixel(x, y, 0)   # make previuos pixel not lit

                            # if next x position is off screen or O key pressed
    if x < 0 or x > 7 or keys & pew.K_O:
        dx = -dx            # reverse its direction

                            # if next x position is off screen or X key pressed
    if y < 0 or y > 7 or keys & pew.K_X:
        dy = -dy            # reverse its direction
    x += dx                 # update x position
    y += dy                 # update y position
    screen.pixel(x, y, 2)   # plot next pixel
    pew.show(screen)        # update screen
    pew.tick(1/12)          # pause approx 1/2 second
