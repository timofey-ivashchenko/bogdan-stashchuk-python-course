import re

from colorama import Fore
from pathlib import Path


def validate_email(email: str) -> None | str:

    file = Path('regex_patterns/email.txt')
    pattern = re.compile(file.read_text())

    if not pattern.fullmatch(email):

        return 'Ошибка в адресе электронной почты.'


def validate_password(password: str) -> None | str:

    if re.compile('\s').search(password):

        return 'Пароль не должен содержать пробелы.'

    if len(password) < 8:

        return 'Длина пароля должна быть не менее 8 символов.'

    if not re.compile('[A-Z]').search(password):

        return 'Пароль должен содержать латинскую букву в верхнем регистре.'

    if not re.compile('[a-z]').search(password):

        return 'Пароль должен содержать латинскую букву в нижнем регистре.'

    if not re.compile('\d').search(password):

        return 'Пароль должен содержать цифру.'

    pattern = '[\[\](){}<>/\\|\.,:;?!`\'"\-=_~@#$%^&*+]'

    if not re.compile(pattern).search(password):

        return 'Пароль должен содержать специальный символ.'


while True:

    email = input(Fore.RESET + 'Введите адрес электронной почты: ' + Fore.BLUE)
    error = validate_email(email)

    if not error:

        print(Fore.GREEN + 'Электронная почта OK.' + Fore.RESET)
        break

    print(Fore.RED + error + Fore.RESET)

while True:

    password = input(Fore.RESET + 'Введите пароль: ' + Fore.BLUE)
    error = validate_password(password)

    if not error:

        print(Fore.GREEN + 'Пароль OK.' + Fore.RESET)
        break

    print(Fore.RED + error + Fore.RESET)

print(Fore.GREEN + 'Регистрация завершена.' + Fore.RESET)
