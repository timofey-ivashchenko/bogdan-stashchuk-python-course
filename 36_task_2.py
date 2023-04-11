def filter_list_1(list_to_filter: list, value_type: type) -> list:
    result = []

    for item in list_to_filter:
        if type(item) is value_type:
            result.append(item)

    return result


def filter_list_2(list_to_filter: list, value_type: type) -> list:
    return list(filter(lambda x: type(x) == value_type, list_to_filter))


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

print(f"{'NoneType':<10}{filter_list_1(source, type(None))}")
print(f"{'bool':<10}{filter_list_1(source, bool)}")
print(f"{'int':<10}{filter_list_1(source, int)}")
print(f"{'float':<10}{filter_list_1(source, float)}")
print(f"{'complex':<10}{filter_list_1(source, complex)}")
print(f"{'str':<10}{filter_list_1(source, str)}")
print(f"{'list':<10}{filter_list_1(source, list)}")
print(f"{'tuple':<10}{filter_list_1(source, tuple)}")
print(f"{'set':<10}{filter_list_1(source, set)}")
print(f"{'dict':<10}{filter_list_1(source, dict)}")
print(f"{'range':<10}{filter_list_1(source, range)}")

print()

print(f"{'NoneType':<9}",
      filter_list_1(source, type(None)) ==
      filter_list_2(source, type(None)))
print(f"{'bool':<9}",
      filter_list_1(source, bool) ==
      filter_list_2(source, bool))
print(f"{'int':<9}",
      filter_list_1(source, int) ==
      filter_list_2(source, int))
print(f"{'float':<9}",
      filter_list_1(source, float) ==
      filter_list_2(source, float))
print(f"{'complex':<9}",
      filter_list_1(source, complex) ==
      filter_list_2(source, complex))
print(f"{'str':<9}",
      filter_list_1(source, str) ==
      filter_list_2(source, str))
print(f"{'list':<9}",
      filter_list_1(source, list) ==
      filter_list_2(source, list))
print(f"{'tuple':<9}",
      filter_list_1(source, tuple) ==
      filter_list_2(source, tuple))
print(f"{'set':<9}",
      filter_list_1(source, set) ==
      filter_list_2(source, set))
print(f"{'dict':<9}",
      filter_list_1(source, dict) ==
      filter_list_2(source, dict))
print(f"{'range':<9}",
      filter_list_1(source, range) ==
      filter_list_2(source, range))
