import csv

from colorama import Fore
from pathlib import Path

# Запись данных в CSV-файл.

data_file = Path('data.csv')

with open(file=data_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow((
        'Name',
        'Description',
        'Category',
        'Price'))
    writer.writerow((
        'Kayak',
        'A boat for one person',
        'Watersports',
        275
    ))
    writer.writerow((
        'Lifejacket',
        'Protective and fashionable',
        'Watersports',
        48.95
    ))
    writer.writerow((
        'Soccer Ball',
        'FIFA-approved size and weight',
        'Soccer',
        19.50
    ))
    writer.writerow((
        'Corner Flags',
        'Give your playing field a professional touch',
        'Soccer',
        34.95
    ))
    writer.writerow((
        'Stadium',
        'Flat-packed 35,000-seat stadium',
        'Soccer',
        79500
    ))
    writer.writerow((
        'Thinking Cap',
        'Improve brain efficiency by 75%',
        'Chess',
        16
    ))
    writer.writerow((
        'Unsteady Chair',
        'Secretly give your opponent a disadvantage',
        'Chess',
        29.95
    ))
    writer.writerow((
        'Human Chess Board',
        'A fun game for the family',
        'Chess',
        75
    ))
    writer.writerow((
        'Bling-Bling King',
        'Gold-plated, diamond-studded King',
        'Chess',
        1200
    ))

print(f"Данные записаны в файл '{data_file}'.")

# Чтение данных из CSV-файла.

print(f"Чтение данных из файла '{data_file}':")

with open(file=data_file, mode='r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(
            Fore.BLUE + row[0],
            Fore.GREEN + row[1],
            Fore.MAGENTA + row[2],
            Fore.YELLOW + row[3],
            Fore.RESET
        )

# Удаление файла данных.

data_file.unlink()
print(f"Файл данных '{data_file}' удалён.")
