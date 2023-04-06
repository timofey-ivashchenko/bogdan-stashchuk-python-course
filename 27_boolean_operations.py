# https://docs.python.org/3/reference/expressions.html#boolean-operations

def get_0() -> int:
    print('Проверяется ложность значения 0...')
    return 0


def get_1() -> int:
    print('Проверяется ложность значения 1...')
    return 1


def get_empty_list() -> list:
    print('Проверяется ложность значения []...')
    return []


def get_nonempty_list() -> list:
    print('Проверяется ложность значения [0]...')
    return [0]


print('*** ОПЕРАТОР and ***')
print('')

# False and False: False
# False and True: False
# Ложность второго операнда не проверяется, возвращается первый операнд.

print('0 and []')
print('Результирующее значение:', get_0() and get_empty_list())
print()

print('[] and 0')
print('Результирующее значение:', get_empty_list() and get_0())
print()

print('0 and 1')
print('Результирующее значение:', get_0() and get_1())
print()

# True and False: False
# True and True: True
# Проверяется ложность обоих операндов, возвращается второй операнд.

print('1 and 0')
print('Результирующее значение:', get_1() and get_0())
print()

print('1 and [0]')
print('Результирующее значение:', get_1() and get_nonempty_list())
print()

print('[0] and 1')
print('Результирующее значение:', get_nonempty_list() and get_1())
print()

print('*** ОПЕРАТОР or ***')
print('')

# True or False: True
# True or True: True
# Ложность второго операнда не проверяется, возвращается первый операнд.

print('1 or 0')
print('Результирующее значение:', get_1() or get_0())
print()

print('1 or [0]')
print('Результирующее значение:', get_1() or get_nonempty_list())
print()

# False or False: False
# False or True: True
# Проверяется ложность обоих операндов, возвращается второй операнд.

print('0 or []')
print('Результирующее значение:', get_0() or get_empty_list())
print()

print('0 or [0]')
print('Результирующее значение:', get_0() or get_nonempty_list())
print()
