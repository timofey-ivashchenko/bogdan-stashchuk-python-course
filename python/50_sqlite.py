import os
import sqlite3

# Устанавливаем соединение с базой данных.

DB_NAME = 'test.db'
connection = sqlite3.connect(DB_NAME)

# Удаляем таблицу courses, если она существует.

sql = 'DROP TABLE IF EXISTS courses'
connection.execute(sql)

# Создаём новую таблицу courses.

sql = '''
CREATE TABLE courses
(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    student_quantity INTEGER,
    review_quantity INTEGER
)
'''

connection.execute(sql)

# Добавляем данные о курсах.

sql = '''
INSERT INTO courses
(
    title,
    student_quantity,
    review_quantity
)
VALUES (?, ?, ?)
'''

courses = (
    ('Полный курс по Python', 1857, 572),
    ('Полный курс по JavaScript', 4141, 1488),
    ('Полный курс по Node.js', 313, 59),
    ('Полный курс по React', 2500, 835),
    ('Полный курс по Docker', 1446, 484),
    ('Курс по Git и GitHub', 319, 93))

for course in courses:
    connection.execute(sql, course)

# Фиксируем изменения в базе данных.

connection.commit()

# Читаем все данные из таблицы courses.

sql = 'SELECT * FROM courses'
result = connection.execute(sql)

print(
    f"{'id':<10}",
    f"{'title':<40}",
    f"{'student_quantity':<20}",
    f"{'review_quantity':<20}")

for row in result:
    print(
        f"{row[0]:<10}",
        f"{row[1]:<40}",
        f"{row[2]:<20}",
        f"{row[3]:<20}")

# Закрываем соединение с базой данных.

connection.close()

# Удаляем базу данных.

os.unlink(DB_NAME)
