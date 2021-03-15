import pygame

pygame.init()

# Variables
gravity = 0.12
thrust = False
thrustVal = 0.24

# Make screen
screen = pygame.display.set_mode((500, 800))
screen.fill((0, 0, 0))
pygame.display.set_caption("Ship Landing")
pygame.display.set_icon(pygame.image.load("shipIcon.png"))

# Background
backLoop1 = pygame.image.load("backLoop800.png")
backLoop2 = pygame.image.load("backLoop800.png")
moon = pygame.image.load("moon800.png")
backY1 = -800
backY2 = 0
backMove = 2

# Player
playerNThrust = pygame.image.load("shipNT128.png")
playerThrust = pygame.image.load("shipThrust128.png")
playerX = 250 - 64
playerY = 0
playerYMove = 0

# Displays the player in its new position
def player(x, y, img):
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    # Show the background for the new frame
    screen.fill((0, 0, 0))
    screen.blit(backLoop1, (0, backY1))
    screen.blit(backLoop2, (0, backY2))
    screen.blit(moon, (0, 0))

    # Applies gravity to the players movement value if the ship isn't at max speed or if the ships isn't at the
    # bottom of the screen.
    if playerYMove != .1 or playerY < 800 - 128:
        playerYMove += gravity

    # Checks for events in the game
    for event in pygame.event.get():
        # Quits the game loop if the player quits the game window
        if event.type == pygame.QUIT:
            running = False
        # Detects key presses
        if event.type == pygame.KEYDOWN:
            # If the up arrow key is pressed, set thrust to "True"
            if event.key == pygame.K_UP:
                thrust = True
        # Detects key releases
        if event.type == pygame.KEYUP:
            # If the up arrow is released, set thrust to "False"
            if event.key == pygame.K_UP:
                thrust = False

    # Player movement
    if thrust:  # Applies thrust to the player if thrust equals "True"
        playerYMove -= thrustVal
    if playerY >= 800 - 128:  # Stops the player from dropping below the screen
        playerY = 800 - 128

    # Gives the player its new position
    playerY += playerYMove

    # Background movement
    # Resets the positions of the background when one drops below the screen
    if backY1 >= 800:
        backY1 = -800
    if backY2 >= 800:
        backY2 = -800

    # Changes the backgrounds position for the next frame
    backY1 += backMove
    backY2 += backMove

    # Draw new positions and update screen
    if thrust:  # Draws the player with thrust image if thrust is "True"
        player(playerX, playerY, playerThrust)
    else:  # Draws the player without thrust image if thrust is "False"
        player(playerX, playerY, playerNThrust)

    # Updates the screen
    pygame.display.update()
