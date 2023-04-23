import re

from colorama import Fore
from pathlib import Path


class CredentialValidator:

    def __get_email_pattern():

        file = Path('regex_patterns/email.txt')
        pattern = file.read_text()
        return re.compile(pattern)

    def __get_password_pattern():

        file = Path('regex_patterns/password.txt')
        pattern = file.read_text()
        return re.compile(pattern)

    email_pattern = __get_email_pattern()
    password_pattern = __get_password_pattern()

    def validate_email(email: str) -> bool:

        return not not CredentialValidator.email_pattern.fullmatch(email)

    def validate_password(password: str) -> bool:

        return not not CredentialValidator.password_pattern.fullmatch(password)


while True:

    email = input('Введите адрес электронной почты: ' + Fore.BLUE)

    if CredentialValidator.validate_email(email):

        print(Fore.GREEN + 'Электронная почта OK.' + Fore.RESET)
        break

    print(Fore.RED + 'Ошибка в электронной почте.' + Fore.RESET)

while True:

    password = input('Введите пароль: ' + Fore.BLUE)

    if CredentialValidator.validate_password(password):

        print(Fore.GREEN + 'Пароль OK.' + Fore.RESET)
        break

    print(Fore.RED + 'Пароль не соответствует требованиям.' + Fore.RESET)

print(Fore.GREEN + 'Регистрация завершена.' + Fore.RESET)
