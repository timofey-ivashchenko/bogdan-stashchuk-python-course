def filter_list(list: list, item_type: type) -> list:
    result = []

    for item in list:
        if type(item) is item_type:
            result.append(item)

    return result


source = [
    # Отсутствие значения.
    None,
    # Логические значения.
    True,
    False,
    # Целые числа.
    1904,
    1930,
    1957,
    1958,
    1980,
    1986,
    2013,
    2015,
    # Числа с плавающей точкой.
    0.25,
    0.50,
    0.75,
    # Комплексные числа.
    123+456j,
    1.2+3.4j,
    # Строки.
    'Слава Україні!',
    'Героям слава!',
    # Списки.
    ['a', 'b', 'c'],
    ['x', 'y', 'z'],
    # Кортежи.
    (1, 2, 5, 10),
    (20, 50, 100),
    # Наборы.
    {0, 2, 4, 6, 8},
    {1, 3, 5, 7, 9},
    # Словари.
    {'a': 1, 'b': 2, 'c': 3},
    {'x': 4, 'y': 5, 'z': 6},
    # Диапазоны.
    range(1991, 2024),
    range(2014, 2024)
]

print(f"{'NoneType':<10}{filter_list(source, type(None))}")
print(f"{'bool':<10}{filter_list(source, bool)}")
print(f"{'int':<10}{filter_list(source, int)}")
print(f"{'float':<10}{filter_list(source, float)}")
print(f"{'complex':<10}{filter_list(source, complex)}")
print(f"{'str':<10}{filter_list(source, str)}")
print(f"{'list':<10}{filter_list(source, list)}")
print(f"{'tuple':<10}{filter_list(source, tuple)}")
print(f"{'set':<10}{filter_list(source, set)}")
print(f"{'dict':<10}{filter_list(source, dict)}")
print(f"{'range':<10}{filter_list(source, range)}")
