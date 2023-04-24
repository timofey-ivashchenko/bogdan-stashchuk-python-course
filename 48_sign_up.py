import re

from colorama import Fore
from pathlib import Path


def validate_email(email: str) -> None | str:

    file = Path('regex_patterns/email.txt')
    pattern = re.compile(file.read_text())

    if not pattern.fullmatch(email):

        return 'Ошибка в адресе электронной почты.'


def validate_password(password: str) -> None | str:

    errors = []

    if re.compile('\s').search(password):

        errors.append('Пароль не должен содержать пробелы.')

    if len(password) < 8:

        errors.append('Длина пароля должна быть не менее 8 символов.')

    if not re.compile('[A-Z]').search(password):

        errors.append(
            'Пароль должен содержать латинскую букву в верхнем регистре.')

    if not re.compile('[a-z]').search(password):

        errors.append(
            'Пароль должен содержать латинскую букву в нижнем регистре.')

    if not re.compile('\d').search(password):

        errors.append('Пароль должен содержать цифру.')

    pattern = '[\[\](){}<>/\\|\.,:;?!`\'"\-=_~@#$%^&*+]'

    if not re.compile(pattern).search(password):

        errors.append('Пароль должен содержать специальный символ.')

    if errors:

        return errors


while True:

    email = input(Fore.RESET + 'Введите адрес электронной почты: ' + Fore.BLUE)
    error = validate_email(email)

    if not error:

        print(Fore.GREEN + 'Электронная почта OK.' + Fore.RESET)
        break

    print(Fore.RED + error + Fore.RESET)

while True:

    password = input(Fore.RESET + 'Введите пароль: ' + Fore.BLUE)
    errors = validate_password(password)

    if not errors:

        print(Fore.GREEN + 'Пароль OK.' + Fore.RESET)
        break

    for error in errors:

        print(Fore.RED + error + Fore.RESET)

print(Fore.GREEN + 'Регистрация завершена.' + Fore.RESET)
