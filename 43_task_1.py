from colorama import Fore
from pathlib import Path

# Создаём каталог.

directory = Path('files')
directory.mkdir(exist_ok=True)
print(f"Каталог '{directory}' создан.")

# Создаём файлы и записываем в них строки из Есенина.

file_1 = directory / 'first.txt'
file_2 = directory / 'second.txt'

content_1 = '''
Белая берёза
Под моим окном
Принакрылась снегом,
Точно серебром.
'''

content_2 = '''
Задремали звёзды золотые,
Задрожало зеркало затона,
Брезжит свет на заводи лесные
И румянит сетку небосклона.
'''

file_1.write_text(content_1.strip(), encoding='utf-8')
print(f"4 строки записаны в файл '{file_1}'.")

file_2.write_text(content_2.strip(), encoding='utf-8')
print(f"4 строки записаны в файл '{file_2}'.")

# Читаем первый файл весь целиком и выводим содержимое в терминал.

with open(file_1, 'r', encoding='utf-8') as file:
    print(f"Читаем содержимое файла '{file_1}' целиком:")
    print(Fore.BLUE + file.read() + Fore.RESET)

# Читаем содержимое второго файла построчно и выводим в терминал.

with open(file_2, 'r', encoding='utf-8') as file:
    print(f"Читаем содержимое файла '{file_2}' построчно:")
    for line in file:
        print(Fore.CYAN + line.rstrip() + Fore.RESET)

# Удаляем файлы и каталог.

file_1.unlink()
print(f"Файл '{file_1}' удалён.")

file_2.unlink()
print(f"Файл '{file_2}' удалён.")

directory.rmdir()
print(f"Каталог '{directory}' удалён.")
