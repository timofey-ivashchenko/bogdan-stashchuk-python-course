import sys

import pygame

# Инициализация игры.
pygame.init()

# Установка заголовка окна.
pygame.display.set_caption('My PyGame')

# Установка размера окна.
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Определение размера и вычисление координат прямоугольника.
rect_width = 100
rect_height = 200
rect_x = (screen_width - rect_width) / 2
rect_y = (screen_height - rect_height) / 2
rect = (rect_x, rect_y, rect_width, rect_height)

# Определение цветов окна и прямоугольника.
screen_color = (2, 84, 100)
rect_color = (232, 170, 66)

# Обработка событий окна.
while True:
    for event in pygame.event.get():
        # Вывод в терминал информации о событии.
        print(event)
        # Завершение работы программы по событию QUIT.
        if event.type == pygame.QUIT:
            sys.exit()
        # Заливка фона окна.
        screen.fill(screen_color)
        # Прорисовка прямоугольника в центре окна.
        pygame.draw.rect(screen, rect_color, rect)
        # Обновление экрана.
        pygame.display.update()
