while True:

    try:

        a = float(input('a: '))

    except ValueError:

        print('Недопустимый ввод.')

        continue

    try:

        b = float(input('b: '))

    except ValueError:

        print('Недопустимый ввод.')

        continue

    if b == 0:

        print('На 0 делить нельзя!')

        continue

    print(f'a / b = {a} / {b} = {a / b}')

    answer = input('Продолжить? (yes/no): ')

    if answer == 'no':

        print('Пока!')

        break
