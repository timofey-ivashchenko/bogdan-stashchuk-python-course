def factorial(n: int) -> int:
    """
    Вычисляет факториал целого положительного числа.

    Args:
        n (int): Целое положительное число.

    Raises:
        TypeError: Если n не целое число.
        ValueError: Если n меньше 1.

    Returns:
        int: Факториал целого положительного числа.
    """

    if type(n) is not int:

        raise TypeError("Аргумент n должен быть целым числом.")

    if n < 1:

        raise ValueError("Число n должно быть больше 0.")

    return n if n == 1 else n * factorial(n - 1)


for n in range(1, 101):

    print(f'{n}! = {factorial(n)}')
