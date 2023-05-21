import sys
from random import randint

import pygame

pygame.init()
pygame.display.set_caption('Awesome Alien Shooter')

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x = (SCREEN_WIDTH - FIGHTER_WIDTH) / 2
FIGHTER_Y = SCREEN_HEIGHT - FIGHTER_HEIGHT
fighter_moving_left, fighter_moving_right = False, False
FIGHTER_STEP = 0.3

BALL_IMAGE = pygame.image.load('images/ball.png')
BALL_WIDTH, BALL_HEIGHT = BALL_IMAGE.get_size()
BALL_X, ball_y = 0, 0
ball_was_fired = False
BALL_STEP = 1

ALIEN_IMAGE = pygame.image.load('images/alien.png')
ALIEN_WIDTH, ALIEN_HEIGHT = ALIEN_IMAGE.get_size()
alien_x, alien_y = 0, 0
alien_was_generated = False
alien_step = 0.05
ALIEN_STEP_INCREASE = 0.005

while True:
    for event in pygame.event.get():
        print(event)
        # Exit the application on the QUIT event.
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Start moving the ship to the left by pressing down the left arrow key.
            if event.key == pygame.K_LEFT:
                fighter_moving_left = True
            # Start moving the ship to the right by pressing down the right arrow key.
            elif event.key == pygame.K_RIGHT:
                fighter_moving_right = True
            # Place the ball directly in front of the ship in the center of the ship.
            elif event.key == pygame.K_SPACE:
                ball_was_fired = True
                BALL_X = fighter_x + (FIGHTER_WIDTH - BALL_WIDTH) / 2
                ball_y = FIGHTER_Y - BALL_HEIGHT
        # Stop moving the ship by pressing up the left or right arrow keys.
        elif event.type == pygame.KEYUP:
            fighter_moving_left = False
            fighter_moving_right = False

    # Move the ship to the left while pressing the left arrow key.
    if fighter_moving_left:
        fighter_x -= FIGHTER_STEP
        if fighter_x < 0:
            fighter_x = 0

    # Move the ship to the right while pressing the right arrow key.
    if fighter_moving_right:
        fighter_x += FIGHTER_STEP
        if fighter_x + FIGHTER_WIDTH > SCREEN_WIDTH:
            fighter_x = SCREEN_WIDTH - FIGHTER_WIDTH

    # Move the ball up.
    if ball_was_fired:
        ball_y -= BALL_STEP
        if ball_y + BALL_HEIGHT < 0:
            ball_was_fired = False

    # Generate the alien.
    if not alien_was_generated:
        alien_x, alien_y = randint(0, SCREEN_WIDTH - ALIEN_WIDTH), 0
        alien_was_generated = True

    # Move the alien down.
    if alien_was_generated:
        alien_y += alien_step
        if alien_y + ALIEN_HEIGHT >= FIGHTER_Y:
            print('Game over.')
            break

    # Shoot the alien.
    if alien_was_generated and \
            ball_was_fired and \
            alien_y + ALIEN_HEIGHT >= ball_y and \
            BALL_X + BALL_WIDTH >= alien_x and \
            BALL_X <= alien_x + ALIEN_WIDTH:
        alien_was_generated = False
        ball_was_fired = False
        # Speed up the new alien.
        alien_step += ALIEN_STEP_INCREASE

    # Render the elements.
    SCREEN.fill((32, 52, 71))
    SCREEN.blit(FIGHTER_IMAGE, (fighter_x, FIGHTER_Y))
    if ball_was_fired:
        SCREEN.blit(BALL_IMAGE, (BALL_X, ball_y))
    if alien_was_generated:
        SCREEN.blit(ALIEN_IMAGE, (alien_x, alien_y))
    pygame.display.update()

# Display the Game Over text.
FONT = pygame.font.Font(None, 30)
GAME_OVER_TEXT = FONT.render('GAME OVER', True, 'white')
GAME_OVER_RECT = GAME_OVER_TEXT.get_rect()
GAME_OVER_RECT.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()
