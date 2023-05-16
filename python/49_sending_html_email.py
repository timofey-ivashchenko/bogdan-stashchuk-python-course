from email.message import EmailMessage
from pathlib import Path
from smtplib import SMTP
from string import Template

# Подготовка электронного письма.

message = EmailMessage()
message['from'] = 'ceo@savoir.com'
message['to'] = 'emilycooper@gmail.com'
message['subject'] = 'Welcome letter'

file = Path('data/welcome_letter.html')
template = Template(file.read_text())
content = template.substitute({
    'annual_salary': '$100,500.00',
    'employee_name': 'Emily Cooper',
    'position': 'Marketing Executive',
    'start_date': 'May 1, 2023'})
message.set_content(content, 'html')

message.add_attachment(
    Path('data/welcome_to_paris.avif').read_bytes(),
    maintype='image', subtype='avif',
    filename='welcome_to_paris.avif')

# Отправка электронного письма.

with SMTP(host='localhost', port=2525) as server:

    server.send_message(message)
    print('Электронное письмо отправлено.')
