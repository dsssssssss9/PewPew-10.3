# Very simple fill screen from l-r , top-bottom using 2 nested loop

import pew

# Intialise Device
pew.init()

# Create Blank Screen Image
screen = pew.Pix()

for y in range(8):
    for x in range(8):
        screen.pixel(x, y, 1)  # plot pixel at x,y brightness 1
        pew.show(screen)  # Update Display
        pew.tick(.25)  # pause .25 seconds


