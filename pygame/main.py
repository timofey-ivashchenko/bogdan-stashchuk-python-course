import sys
from random import randint

import pygame

# Initialize the game.
pygame.init()
# Set the window caption.
pygame.display.set_caption('My PyGame')
# Set the window size.
screen = pygame.display.set_mode((800, 600))

# Handle the window events.
while True:
    for event in pygame.event.get():
        # Print the event info.
        print(event)
        # Exit on the QUIT event.
        if event.type == pygame.QUIT:
            sys.exit()
        # Set the background color of the window to a random color.
        screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
        pygame.display.update()
