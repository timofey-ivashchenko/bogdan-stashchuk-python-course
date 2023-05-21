import sys

import pygame

pygame.init()
pygame.display.set_caption('Pygame Shooter')

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
fighter_x = (SCREEN_WIDTH - FIGHTER_WIDTH) / 2
FIGHTER_Y = SCREEN_HEIGHT - FIGHTER_HEIGHT

while True:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill((32, 52, 71))
    SCREEN.blit(FIGHTER_IMAGE, (fighter_x, FIGHTER_Y))
    pygame.display.update()
