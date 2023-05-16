def greeting(greet):
    return lambda name: f'{greet}, {name}!'


morning_greeting = greeting('Доброе утро')
afternoon_greeting = greeting('Добрый день')
evening_greeting = greeting('Добрый вечер')
night_greeting = greeting('Спокойной ночи')

print(morning_greeting('Наташа'))
print(afternoon_greeting('Вова'))
print(evening_greeting('Паша'))
print(night_greeting('Егор'))
print(night_greeting('Ваня'))
