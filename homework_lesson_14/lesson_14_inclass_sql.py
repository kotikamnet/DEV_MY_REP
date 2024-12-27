"""
Создайте базу данных:

Назовите её library.db.
Создайте таблицу books: Таблица должна содержать следующие поля:

id — уникальный идентификатор книги (целое число, PRIMARY KEY, AUTOINCREMENT).
title — название книги (текст).
author — автор книги (текст).
year — год выпуска (целое число).
available — доступность книги (логическое значение: 1 — доступна, 0 — недоступна).
Добавьте данные в таблицу: Вставьте 5 записей в таблицу books, например:


1. "1984", George Orwell, 1949, доступна
2. "To Kill a Mockingbird", Harper Lee, 1960, доступна
3. "The Great Gatsby", F. Scott Fitzgerald, 1925, недоступна
4. "Moby Dick", Herman Melville, 1851, доступна
5. "War and Peace", Leo Tolstoy, 1869, недоступна
Выполните запросы:

Выберите все книги, которые доступны.
Найдите книги, выпущенные после 1950 года.
Обновите доступность книги "The Great Gatsby" на "доступна".
Удалите из таблицы книгу "Moby Dick".
Сохраните изменения: Убедитесь, что данные сохраняются в базе после выполнения запросов.
"""

import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('../lesson_12/library.db')
cursor = connection.cursor()

# Создаем таблицу books
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    available INTEGER NOT NULL
)
""")

# Данные для вставки
books_data = [
    ("1984", "George Orwell", 1949, 1),
    ("To Kill a Mockingbird", "Harper Lee", 1960, 1),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, 0),
    ("Moby Dick", "Herman Melville", 1851, 1),
    ("War and Peace", "Leo Tolstoy", 1869, 0)
]

# Вставка данных (добавление новых записей, если их еще нет)
cursor.executemany("""
INSERT OR IGNORE INTO books (title, author, year, available) 
VALUES (?, ?, ?, ?)
""", books_data)

connection.commit()

# 1. Выберите все книги, которые доступны
print("\nДоступные книги:")
cursor.execute("SELECT * FROM books WHERE available = 1")
available_books = cursor.fetchall()
for book in available_books:
    print(book)

# 2. Найдите книги, выпущенные после 1950 года
print("\nКниги, выпущенные после 1950 года:")
cursor.execute("SELECT title, year FROM books WHERE year > ?", (1950,))
recent_books = cursor.fetchall()
for book in recent_books:
    print(book)

# 3. Обновите доступность книги "The Great Gatsby" на "доступна"
cursor.execute("UPDATE books SET available = 1 WHERE title = ?", ("The Great Gatsby",))
connection.commit()
print("\nКнига 'The Great Gatsby' теперь доступна.")

# 4. Удалите из таблицы книгу "Moby Dick"
cursor.execute("DELETE FROM books WHERE title = ?", ("Moby Dick",))
connection.commit()
print("\nКнига 'Moby Dick' была удалена.")

# 5. Проверьте финальное состояние таблицы
print("\nФинальное состояние таблицы:")
cursor.execute("SELECT * FROM books")
all_books = cursor.fetchall()
for book in all_books:
    print(book)

# Закрытие соединения
connection.close()
