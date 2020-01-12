#  Very simple program to display random pixels each with random brightness
import pew
import random

pew.init()                    # intialise device
screen = pew.Pix()            # create empty screen image

delay =  1 / 16                   # approx delay time in seconds for loop

while True:
    x = random.randint(0, 7)  # choose random column from 0 to 7
    y = random.randint(0, 7)  # choose random row from 0 to 7
    b = random.randint(0, 3)  # choose random brightness from 0 to 3
    screen.pixel(x, y, b)     # display pixel at colum x, row y , brightness b
    pew.show(screen)          # update screen
    pew.tick(delay)           # pause for delay seconds
