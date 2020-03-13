# 6 Sided die - graphic display = press X for next number

from random import randint  # import random integer function

import pew  # Import pewpew library

pew.init()  # Initlise library

screen = pew.Pix()  # Create blsnk screen

# Define pattern for 1 dot
score1 = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

# Define pattern for 2 dots
score2 = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 1, 0, 0, 0, 0, 0),
    (0, 1, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 1, 0),
    (0, 0, 0, 0, 0, 1, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

# Define pattern for 3 dots
score3 = pew.Pix.from_iter((
    (1, 1, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 1, 1),
))

# Define pattern for 4 dots
score4 = pew.Pix.from_iter((
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
))

# Define pattern for 5 dots
score5 = pew.Pix.from_iter((
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
))

# Define pattern for 6 dots
score6 = pew.Pix.from_iter((
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 1, 1),
))

while True:
    pew.tick(1)   # pause 1 second

    key = pew.keys()  # read key press

    if key & pew.K_X:  # if X key pressed...
        dice = randint(1, 6)  # Pick random integer from 1 to 6

        if dice == 1:
            screen.blit(score1)  # if ==1 choose 1 dot pattern

        elif dice == 2:
            screen.blit(score2)  # if ==2 choose 2 dot pattern

        elif dice == 3:
            screen.blit(score3)  # if ==3 choose 3 dot pattern

        elif dice == 4:
            screen.blit(score4)  # if ==4 choose 4 dot pattern

        elif dice == 5:
            screen.blit(score5)  # if ==5 choose 5 dot pattern

        elif dice == 6:
            screen.blit(score6)  # if ==6 choose 6 dot pattern

    pew.show(screen)  # Display Screen content
    pew.tick(1)   # Pause 1 Second