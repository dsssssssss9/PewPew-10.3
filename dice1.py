# Simple text 6 Sided Die - Press X key for next number

# Import random integer function
from random import randint

# Import Pew Library
import pew

# Initialise Device
pew.init()


while True:
    # Pause 1 second
    pew.tick(1)
    # read key press
    key = pew.keys()

    if key & pew.K_X:  # if X key pressed...
        dice = randint(1, 6)  # Picj random integer from 1 to 6
        if dice == 1:
            screen = pew.Pix.from_text("1")  # if ==1 set text to "1"

        elif dice == 2:
            screen = pew.Pix.from_text("2")   # if ==2 set text to "2"

        elif dice == 3:
            screen = pew.Pix.from_text("3")  # if ==3 set text to "3"

        elif dice == 4:
            screen = pew.Pix.from_text("4")  # if ==4 set text to "4"

        elif dice == 5:
            screen = pew.Pix.from_text("5")  # if ==5 set text to "5"

        elif dice == 6:
            screen = pew.Pix.from_text("6")  # if ==6 set text to "6"

    pew.show(screen)  # Display text
    pew.tick(1)   # Pause 1 Second