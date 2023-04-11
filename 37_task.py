while True:

    a = float(input('a: '))
    b = float(input('b: '))

    if b == 0:

        print('На 0 делить нельзя!')

        continue

    print(f'a / b = {a} / {b} = {a / b}')

    answer = input('Продолжить? (yes/no): ')

    if answer == 'no':

        print('Пока!')

        break
