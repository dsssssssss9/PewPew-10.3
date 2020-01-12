#  Simple demo usuing blit to copy alternating pattern to screen
import pew

# Intialise Device
pew.init()

# Create Blank Screen Image
screen = pew.Pix()

# Set Loop Delay Value in Seconds
delay = 1/6


# Setup String to hold pattern to be used as background
background = pew.Pix.from_iter((
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
))

# Setup String to hold pattern to be used as second background
background2 = pew.Pix.from_iter((
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0),
))

# Loop Forever
while True:
    # Copy Image Stored in ( background ) to screen
    screen.blit(background)

    # Update Screen
    pew.show(screen)

    # Pause
    pew.tick(delay)

    # Copy Image Stored in ( background2 ) to screen
    screen.blit(background2)

    # Update Screen
    pew.show(screen)

    # Pause
    pew.tick(delay)
