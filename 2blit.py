# Simple box decreasing toward center usin blit


import pew

# Intialise Device
pew.init()

# Create Blank Screen Image
screen = pew.Pix()

# Set Loop Delay Value in Seconds
delay = 1/2

# Setup sring to hold blank screen
sb = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

# Setup string all outer pixels
s0 = pew.Pix.from_iter((
    (1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1),
))

# Setup string move next layr in
s1 = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 1, 1, 1, 1, 1, 0),
    (0, 1, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 0, 0, 0, 1, 0),
    (0, 1, 0, 0, 0, 0, 1, 0),
    (0, 1, 1, 1, 1, 1, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

# Setup string 3rd layer
s2 = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 0, 0, 2, 0, 0),
    (0, 0, 2, 0, 0, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))

# Setup string middle 4 pixels - Max Brightness
s3 = pew.Pix.from_iter((
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 3, 3, 0, 0, 0),
    (0, 0, 0, 3, 3, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0),
))


# Loop Forever
while True:
    # Copy Image Stored in ( s0 ) to screen
    screen.blit(s0)

    # Update Screen
    pew.show(screen)

    # Pause
    pew.tick(delay)

    # Copy Image Stored in ( s1 ) to screen
    screen.blit(s1)

    # Update Screen
    pew.show(screen)

    pew.tick(delay)

# Copt image stored in s2
    screen.blit(s2)

    pew.show(screen)

    # Pause
    pew.tick(delay)

    # Copy Image Stored in ( s3 ) to screen

    screen.blit(s3)

    pew.show(screen)


# iterate 9 times beteen blank screen & s3
    for index in range(7):
        screen.blit(sb)
        pew.show(screen)
        pew.tick(delay / 8)
        screen.blit(s3)
        pew.show(screen)
        pew.tick(delay / 8)

    # Pause
    pew.tick(delay)
