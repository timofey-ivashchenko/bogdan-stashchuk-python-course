import sys

import pygame

# Initialize the game.
pygame.init()

# Set the window caption.
pygame.display.set_caption('Move the Rectangle')

# Set the size of the window.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the size of the rectangle.
RECT_WIDTH = 100
RECT_HEIGHT = 200

# Calculate the initial coordinates of the rectangle:
# place in the center of the window.
rect_x = (SCREEN_WIDTH - RECT_WIDTH) / 2
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) / 2

# The colors of the window and rectangle.
SCREEN_COLOR = (2, 84, 100)
RECT_COLOR = (232, 170, 66)

# The rectangle offset step.
STEP = 50

# Process window events.
while True:
    for event in pygame.event.get():
        # Print the event information in the terminal.
        print(event)
        # End the program on the QUIT event.
        if event.type == pygame.QUIT:
            sys.exit()
        # Pressing a key on the keyboard.
        elif event.type == pygame.KEYDOWN:
            # Left arrow.
            if event.key == pygame.K_LEFT:
                if rect_x - STEP >= 0:
                    rect_x -= STEP
            # Right arrow.
            elif event.key == pygame.K_RIGHT:
                if rect_x + RECT_WIDTH + STEP <= SCREEN_WIDTH:
                    rect_x += STEP
            # Up arrow.
            elif event.key == pygame.K_UP:
                if rect_y - STEP >= 0:
                    rect_y -= STEP
            # Down arrow.
            elif event.key == pygame.K_DOWN:
                if rect_y + RECT_HEIGHT + STEP <= SCREEN_HEIGHT:
                    rect_y += STEP
        # Fill the window background.
        SCREEN.fill(SCREEN_COLOR)
        # Draw the rectangle.
        rect = (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
        pygame.draw.rect(SCREEN, RECT_COLOR, rect)
        # Update the display.
        pygame.display.update()
