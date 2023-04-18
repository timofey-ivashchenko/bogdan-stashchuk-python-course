import os

from colorama import Fore
from pathlib import Path

# Создаём каталог.

directory = Path('files')

if not directory.exists():
    os.mkdir(directory)
    print(f"Каталог '{directory}' создан.")

# Создаём файлы и записываем в них строки из Есенина.

file_1 = directory / 'first.txt'
file_2 = directory / 'second.txt'

if not file_1.exists():
    with open(file_1, 'w', encoding='utf-8') as file:
        print(f"Файл '{file_1}' создан.")
        file.write('Белая берёза\n')
        file.write('Под моим окном\n')
        file.write('Принакрылась снегом,\n')
        file.write('Точно серебром.')
        print(f"4 строки записаны в файл '{file_1}'.")

if not file_2.exists():
    with open(file_2, 'w', encoding='utf-8') as file:
        print(f"Файл '{file_2}' создан.")
        file.write('Задремали звёзды золотые,\n')
        file.write('Задрожало зеркало затона,\n')
        file.write('Брезжит свет на заводи речные\n')
        file.write('И румянит сетку небосклона.')
        print(f"4 строки записаны в файл '{file_2}'.")

# Читаем первый файл весь целиком и выводим содержимое в терминал.

with open(file_1, 'r', encoding='utf-8') as file:
    print(f"Читаем содержимое файла '{file_1}' целиком:")
    print(Fore.BLUE + file.read() + Fore.RESET)

# Читаем содержимое второго файла построчно и выводим в терминал.

with open(file_2, 'r', encoding='utf-8') as file:
    print(f"Читаем содержимое файла '{file_2}' построчно:")
    while True:
        line = file.readline()
        if not line:
            break
        print(Fore.CYAN + line.rstrip() + Fore.RESET)

# Удаляем файлы и каталог.

if file_1.exists():
    file_1.unlink()
    print(f"Файл '{file_1}' удалён.")

if file_2.exists():
    file_2.unlink()
    print(f"Файл '{file_2}' удалён.")

if directory.exists():
    os.rmdir(directory)
    print(f"Каталог '{directory}' удалён.")
