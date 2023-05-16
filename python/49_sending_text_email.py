from email.message import EmailMessage
from pathlib import Path
from smtplib import SMTP

# Создание электронного письма.

message = EmailMessage()
message['from'] = 'timofey.ivashchenko@gmail.com'
message['to'] = 'tymofii.ivashchenko@gmail.com'
message['subject'] = 'The Zen of Python'

file = Path('data/the_zen_of_python.txt')
content = file.read_text(encoding='utf-8')
message.set_content(content)

# Отправка электронного письма.

with SMTP(host='localhost', port=2525) as server:

    server.send_message(message)
    print('Электронное письмо отправлено.')
