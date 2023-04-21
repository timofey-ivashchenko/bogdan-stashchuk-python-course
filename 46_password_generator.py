import secrets
import string

from colorama import Fore

all_chars = string.ascii_letters + string.digits + string.punctuation


def generate_password(length: int, chars: str = None) -> str:
    return ''.join(secrets.choice(chars or all_chars) for _ in range(length))


print(f"{'Все символы:':<32}",
      Fore.RED + generate_password(64) + Fore.RESET)
print(f"{'Все буквы ASCII:':<32}",
      Fore.YELLOW + generate_password(64, string.ascii_letters) + Fore.RESET)
print(f"{'Буквы ASCII в нижнем регистре:':<32}",
      Fore.GREEN + generate_password(64, string.ascii_lowercase) + Fore.RESET)
print(f"{'Буквы ASCII в верхнем регистре:':<32}",
      Fore.CYAN + generate_password(64, string.ascii_uppercase) + Fore.RESET)
print(f"{'Цифры:':<32}",
      Fore.BLUE + generate_password(64, string.digits) + Fore.RESET)
print(f"{'Шестнадцатеричные цифры:':<32}",
      Fore.MAGENTA + generate_password(64, string.hexdigits) + Fore.RESET)
print(f"{'Восьмеричные цифры:':<32}",
      Fore.RED + generate_password(64, string.octdigits) + Fore.RESET)
print(f"{'Знаки пунктуации:':<32}",
      Fore.YELLOW + generate_password(64, string.punctuation) + Fore.RESET)
