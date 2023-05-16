import sys

from array import array
from colorama import Fore
from pathlib import Path

# Пользователь не указал путь к файлу.

if len(sys.argv) < 2:
    error = 'Не указан путь к файлу.'
    print(Fore.RED + error + Fore.RESET)
    exit()

# Указанный файл не существует.

path = Path(sys.argv[1])

if not path.exists():
    error = f"Файл '{path}' не найден."
    print(Fore.RED + error + Fore.RESET)
    exit()

# Загружаем данные в массив и выводим массив в терминал.

numbers = array('i')

with open(path, 'rb') as file:
    file_size = path.stat().st_size
    number_count = file_size // 4
    numbers.fromfile(file, number_count)

print(
    Fore.CYAN + 'numbers:' + Fore.RESET,
    Fore.GREEN + str(numbers) + Fore.RESET)
