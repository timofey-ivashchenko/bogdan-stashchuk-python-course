# https://docs.python.org/3/reference/simple_stmts.html#the-del-statement

def test_parameter_deletion(x):
    'x' in dir() and print('Параметр x существует.')

    del x

    'x' not in dir() and print('Параметр x не существует.')


# Удаление элемента последовательности.

cities = {'Киев': 'UTC+2', 'Москва': 'UTC+3', 'Нью-Йорк': 'UTC-5'}

'Москва' in cities and print("Элемент 'Москва' существует.")

del cities['Москва']

'Москва' not in cities and print("Элемент 'Москва' не существует.")

# Удаление пользовательского объекта.

x = 0

'x' in dir() and print('Переменная x существует.')

del x

'x' not in dir() and print('Переменная x не существует.')

# Удаление встроенного объекта.

'__builtins__' in dir() and print(
    'Встроенный объект __builtins__ существует.')

del __builtins__

'__builtins__' not in dir() and print(
    'Встроенный объект __builtins__ не существует.')

# Удаление параметра функции.

test_parameter_deletion(0)
