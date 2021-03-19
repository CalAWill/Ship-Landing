import pygame
import time

pygame.init()

# Make screen
screen = pygame.display.set_mode((500, 800))
screen.fill((0, 0, 0))
pygame.display.set_caption("Ship Landing")
pygame.display.set_icon(pygame.image.load("shipIcon.png"))

# Replay text code
replayFont = pygame.font.Font("freesansbold.ttf", 64)
replayText = replayFont.render("REPLAY?", True, (255, 255, 255))
winText = replayFont.render("YOU WIN", True, (255, 255, 255))
loseText = replayFont.render("YOU LOSE", True, (255, 255, 255))

# Button text
yesNoFont = pygame.font.Font("freesansbold.ttf", 32)
yesText = yesNoFont.render("YES", True, (255, 255, 255))
noText = yesNoFont.render("NO", True, (255, 255, 255))


# Displays the player in its new position
def player(x, y, img):
    screen.blit(img, (x, y))


def game():
    # Background
    backLoop1 = pygame.image.load("backLoop800.png")
    backLoop2 = pygame.image.load("backLoop800.png")
    moon = pygame.image.load("moon800.png")
    backY1 = -800
    backY2 = 0
    backMove = 2

    # Variables
    gravity = 0.12
    thrust = False
    thrustVal = 0.24

    # Player
    playerNThrust = pygame.image.load("shipNT128.png")
    playerThrust = pygame.image.load("shipThrust128.png")
    playerX = 250 - 64
    playerY = 0
    playerYMove = 0

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
        for gameEvent in pygame.event.get():
            # Quits the game loop if the player quits the game window
            if gameEvent.type == pygame.QUIT:
                running = False
            # Detects key presses
            if gameEvent.type == pygame.KEYDOWN:
                # If the up arrow key is pressed, set thrust to "True"
                if gameEvent.key == pygame.K_UP:
                    thrust = True
            # Detects key releases
            if gameEvent.type == pygame.KEYUP:
                # If the up arrow is released, set thrust to "False"
                if gameEvent.key == pygame.K_UP:
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

        print(playerYMove)
        # Check if the player has won or lost
        if playerYMove >= 3 and playerY >= 800 - 128:
            # Displays the win text and waits 1 second
            screen.blit(loseText, (100, 250))
            pygame.display.update()
            time.sleep(1)
            running = False
        if playerYMove < 3 and playerY >= 800 - 128:
            # Displays the lose text and then waits 1 second
            screen.blit(winText, (100, 250))
            pygame.display.update()
            time.sleep(1)
            running = False

        # Updates the screen
        pygame.display.update()


game()

GUIrunning = True
while GUIrunning:
    # Gets the mouse x and y position
    mousePos = pygame.mouse.get_pos()

    # Refreshes the screen to black so updates can be made
    screen.fill((0, 0, 0))

    # Puts the boxes and text on screen
    screen.blit(replayText, (100, 250))

    # Looks for events
    for event in pygame.event.get():
        # If the player presses the exit window button, then quit the program
        if event.type == pygame.QUIT:
            GUIrunning = False
        # If the player clicks, check if they've clicked over one of the buttons
        if event.type == pygame.MOUSEBUTTONUP:
            # Have they clicked over the "yes" button? If so, call the ping() method
            if 225 < mousePos[0] < 325 and 325 < mousePos[1] < 375:
                game()
            # Have they clicked over the "no" button? If so, exit the loop and program as a result
            if 375 < mousePos[0] < 475 and 325 < mousePos[1] < 375:
                GUIrunning = False

    # If the mouse is over the yes box or no box, change the colour
    if 225 < mousePos[0] < 325 and 325 < mousePos[1] < 375:
        pygame.draw.rect(screen, (115, 255, 152), (225, 325, 100, 50))
    else:
        pygame.draw.rect(screen, (255, 255, 255), (225, 325, 100, 50))

    if 375 < mousePos[0] < 475 and 325 < mousePos[1] < 375:
        pygame.draw.rect(screen, (255, 97, 102), (375, 325, 100, 50))
    else:
        pygame.draw.rect(screen, (255, 255, 255), (375, 325, 100, 50))

    # Adds the "yes" and "no" text to the buttons
    screen.blit(yesText, (225, 325))
    screen.blit(noText, (375, 325))

    # Updates the screen on every loop
    pygame.display.update()
