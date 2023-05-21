import sys

import pygame

pygame.init()
pygame.display.set_caption('Awesome Alien Shooter')

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x = (SCREEN_WIDTH - FIGHTER_WIDTH) / 2
FIGHTER_Y = SCREEN_HEIGHT - FIGHTER_HEIGHT
moving_left, moving_right = False, False
STEP = 1

BALL_IMAGE = pygame.image.load('images/ball.png')
BALL_WIDTH, BALL_HEIGHT = BALL_IMAGE.get_size()
BALL_X, ball_y = 0, 0
ball_was_fired = False

while True:
    for event in pygame.event.get():
        print(event)
        # Exit the application on the QUIT event.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Start moving the ship to the left by pressing down the left arrow key.
            if event.key == pygame.K_LEFT:
                moving_left = True
            # Start moving the ship to the right by pressing down the right arrow key.
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            # Place the ball directly in front of the ship in the center of the ship.
            elif event.key == pygame.K_SPACE:
                ball_was_fired = True
                BALL_X = fighter_x + (FIGHTER_WIDTH - BALL_WIDTH) / 2
                ball_y = FIGHTER_Y - BALL_HEIGHT
        # Stop moving the ship by pressing up the left or right arrow keys.
        elif event.type == pygame.KEYUP:
            moving_left = False
            moving_right = False

    # Move the ship to the left while pressing the left arrow key.
    if moving_left:
        fighter_x -= STEP
        if fighter_x < 0:
            fighter_x = 0

    # Move the ship to the right while pressing the right arrow key.
    if moving_right:
        fighter_x += STEP
        if fighter_x + FIGHTER_WIDTH > SCREEN_WIDTH:
            fighter_x = SCREEN_WIDTH - FIGHTER_WIDTH

    # Render the elements.
    SCREEN.fill((32, 52, 71))
    SCREEN.blit(FIGHTER_IMAGE, (fighter_x, FIGHTER_Y))
    if ball_was_fired:
        SCREEN.blit(BALL_IMAGE, (BALL_X, ball_y))
    pygame.display.update()
