import sys

import pygame

# Инициализация игры.
pygame.init()

# Установка заголовка окна.
pygame.display.set_caption('Перемещаем прямоугольник')

# Установка размера окна.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Определение размера прямоугольника.
RECT_WIDTH = 100
RECT_HEIGHT = 200

# Вычисление начальных координат прямоугольника:
# размещение по центру окна.
rect_x = (SCREEN_WIDTH - RECT_WIDTH) / 2
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) / 2

# Цвета окна и прямоугольника.
SCREEN_COLOR = (2, 84, 100)
RECT_COLOR = (232, 170, 66)

# Шаг смещения прямоугольника.
STEP = 50

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
                if rect_x - STEP >= 0:
                    rect_x -= STEP
            # Стрелка вправо.
            elif event.key == pygame.K_RIGHT:
                if rect_x + RECT_WIDTH + STEP <= SCREEN_WIDTH:
                    rect_x += STEP
            # Стрелка вверх.
            elif event.key == pygame.K_UP:
                if rect_y - STEP >= 0:
                    rect_y -= STEP
            # Стрелка вниз.
            elif event.key == pygame.K_DOWN:
                if rect_y + RECT_HEIGHT + STEP <= SCREEN_HEIGHT:
                    rect_y += STEP
        # Заливка фона окна.
        SCREEN.fill(SCREEN_COLOR)
        # Прорисовка прямоугольника.
        rect = (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT)
        pygame.draw.rect(SCREEN, RECT_COLOR, rect)
        # Обновление экрана.
        pygame.display.update()
