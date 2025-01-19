'''
Задача 1: Создание и заполнение таблиц
● Создайте таблицу authors с полями id, first_name и last_name. Используйте PRIMARY KEY для поля id
● Создайте таблицу books с полями id, title, author_id и publication_year.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для поля author_id, ссылаясь на таблицу authors
● Создайте таблицу sales с полями id, book_id и quantity.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для поля book_id, ссылаясь на таблицу books
● Добавьте несколько авторов в таблицу authors
● Добавьте несколько книг в таблицу books, указывая авторов из таблицы authors
● Добавьте записи о продажах книг в таблицу sales
'''

import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('../lesson_15/bookshop.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    publication_year INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id)
)
''')

authors_data = [
    ('Harper', 'Lee'),
    ('Leo', 'Tolstoy'),
    ('Herman', 'Melville'),
    ('George', 'Orwell'),
    ('F. Scott', 'Fitzgerald')
]
cursor.executemany('''
INSERT INTO authors (first_name, last_name)
VALUES (?, ?)
''', authors_data)


books_data = [
    ('To Kill a Mockingbird', 1, 1960),
    ('War and Peace', 2, 1869),
    ('Moby Dick', 3, 1851),
    ('1984', 4, 1949),
    ('The Great Gatsby', 5, 1925)
]
cursor.executemany('''
INSERT INTO books (title, author_id, publication_year)
VALUES (?, ?, ?)
''', books_data)

sales_data = [
    (1, 6),
    (2, 10),
    (3, 3),
    (4, 1),
    (5, 12)
]
cursor.executemany('''
INSERT INTO sales (book_id, quantity)
VALUES (?, ?)
''', sales_data)

connection.commit()
connection.close()
