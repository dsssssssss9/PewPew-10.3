# Simple moving dot from random start position
import pew
from random import randint

pew.init()                  # intialise device
screen = pew.Pix()          # create empty screen image

x = randint(0, 7)           # random intial x position
y = randint(0, 7)           # random intial y position


dx = 1                      # initial x step
dy = 1                      # initial y step

while True:
    screen.pixel(x, y, 0)   #make previuos pixel not lit
    if x < 0 or x > 7:      #if next x position is off screen
        dx = -dx            #reverse its direction
    if y < 0 or y > 7:      #if next y position is off screen
        dy = -dy            #reverse its direction
    x += dx                 #update x position
    y += dy                 #update y position
    screen.pixel(x, y, 2)   #plot next pixel
    pew.show(screen)        #update screen
    pew.tick(1/12)          #pause approx 1/2 second
