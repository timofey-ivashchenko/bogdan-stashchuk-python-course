import re

from colorama import Fore
from pathlib import Path


class CredentialValidator:

    def __init__(self):

        file = Path('regex_patterns/email.txt')
        pattern = file.read_text()
        self.email_pattern = re.compile(pattern)

        file = Path('regex_patterns/password.txt')
        pattern = file.read_text()
        self.password_pattern = re.compile(pattern)

    def validate_email(self, email: str) -> bool:

        return not not self.email_pattern.fullmatch(email)

    def validate_password(self, password: str) -> bool:

        return not not self.password_pattern.fullmatch(password)


validator = CredentialValidator()

while True:

    email = input('Введите адрес электронной почты: ' + Fore.BLUE)

    if validator.validate_email(email):

        print(Fore.GREEN + 'Электронная почта OK.' + Fore.RESET)
        break

    print(Fore.RED + 'Ошибка в электронной почте.' + Fore.RESET)

while True:

    password = input('Введите пароль: ' + Fore.BLUE)

    if validator.validate_password(password):

        print(Fore.GREEN + 'Пароль OK.' + Fore.RESET)
        break

    print(Fore.RED + 'Пароль не соответствует требованиям.' + Fore.RESET)

print(Fore.GREEN + 'Регистрация завершена.' + Fore.RESET)
