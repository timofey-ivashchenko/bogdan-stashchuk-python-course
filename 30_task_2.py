band_name = 'The Beatles'
album_name = 'Abbey Road'
album_year = 1969
million_copies_sold = 19.9
personnel = [
    'Джон Леннон',
    'Пол Маккартни',
    'Джордж Харрисон',
    'Ринго Старр',
    'Джордж Мартин',
    'Билли Престон']

info = f'''{album_name.upper()} / {band_name.upper()}

Последняя и лучшая запись группы.
Альбом был записан в одноимённой студии с 22 февраля по 19 августа {album_year} года.
По состоянию на апрель 2023 года общие продажи по всему миру составили {million_copies_sold} миллионов копий.

Участники записи:

{str(personnel).strip("[]").replace("'", '')}'''

print(info)
