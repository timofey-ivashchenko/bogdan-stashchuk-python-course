image_size = (1920, 1080)

info_1 = f'{image_size[0]}x{image_size[1]}' if len(
    image_size) == 2 else 'Неправильный размер изображения'

if len(image_size) == 2:
    info_2 = f'{image_size[0]}x{image_size[1]}'
else:
    info_2 = 'Неправильный размер изображения'

print('info_1:', info_1)
print('info_2:', info_2)
print('info_1 == info_2:', info_1 == info_2)
