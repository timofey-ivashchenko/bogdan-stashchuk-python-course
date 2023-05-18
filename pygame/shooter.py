import sys

import pygame

# Инициализация игры.
pygame.init()

# Установка заголовка окна.
pygame.display.set_caption('Pygame Shooter')

# Установка размера окна.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Обработка событий окна.
while True:
    for event in pygame.event.get():
        # Вывод в терминал информации о событии.
        print(event)
        # Завершение работы программы по событию QUIT.
        if event.type == pygame.QUIT:
            sys.exit()
