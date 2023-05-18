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

# Определение размера прямоугольника.
rect_width = 100
rect_height = 200

# Вычисление начальных координат прямоугольника:
# размещение по центру окна.
rect_x = (screen_width - rect_width) / 2
rect_y = (screen_height - rect_height) / 2

# Цвета окна и прямоугольника.
screen_color = (2, 84, 100)
rect_color = (232, 170, 66)

# Шаг смещения прямоугольника.
step = 50

# Обработка событий окна.
while True:
    for event in pygame.event.get():
        # Вывод в терминал информации о событии.
        print(event)
        # Завершение работы программы по событию QUIT.
        if event.type == pygame.QUIT:
            sys.exit()
        # Нажатие клавиши на клавиатуре.
        elif event.type == pygame.KEYDOWN:
            # Стрелка влево.
            if event.key == pygame.K_LEFT:
                rect_x -= step
            # Стрелка вправо.
            elif event.key == pygame.K_RIGHT:
                rect_x += step
            # Стрелка вверх.
            elif event.key == pygame.K_UP:
                rect_y -= step
            # Стрелка вниз.
            elif event.key == pygame.K_DOWN:
                rect_y += step
        # Заливка фона окна.
        screen.fill(screen_color)
        # Прорисовка прямоугольника.
        rect = (rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, rect)
        # Обновление экрана.
        pygame.display.update()
