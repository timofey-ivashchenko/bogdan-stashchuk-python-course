def get_image_info(image: dict) -> str:
    if 'image_id' not in image:
        raise ValueError("Аргумент 'image' не содержит ключ 'image_id'.")

    if 'image_title' not in image:
        raise ValueError("Аргумент 'image' не содержит ключ 'image_title'.")

    id = image['image_id']
    title = image['image_title']

    return f"Изображение '{title}' имеет идентификатор {id}."


def print_image_info(**image: dict) -> None:
    try:
        print(get_image_info(image))
    except ValueError as error:
        print(f'ValueError: {str(error)}')


print_image_info(image_id=123, image_title='Мой любимый кот')
print_image_info(image_title='Мой любимый кот')
print_image_info(image_id=123)
print_image_info()
