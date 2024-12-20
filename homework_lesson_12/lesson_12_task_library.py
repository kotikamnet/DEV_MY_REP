"""
Задача: Управление библиотекой
Описание:

Создайте приложение для управления виртуальной библиотекой.
В библиотеке есть книги, которые могут быть взяты на чтение или возвращены.
Книги имеют следующие характеристики:

Название
Автор
Год издания
Уникальный идентификатор (например, id)
Статус (доступна/взята)
Требования:

Класс Book:
Свойства: title, author, year, isbn, is_available.
Методы:
borrow(): меняет статус книги на "взята".
return_book(): меняет статус книги на "доступна".


Класс Library:
Свойства:
books — список объектов Book.
Методы:
add_book(book): добавляет книгу в библиотеку.
remove_book(isbn): удаляет книгу из библиотеки по ISBN.
find_books_by_author(author): возвращает список книг автора.
list_available_books(): выводит список всех доступных книг.
borrow_book(isbn): выдает книгу по ISBN, если она доступна.
return_book(isbn): возвращает книгу в библиотеку.

Напишите программу, которая:
Создает библиотеку.
Добавляет в нее несколько книг.
Позволяет пользователю взаимодействовать с библиотекой через меню
(например, брать книги, возвращать, искать по автору и т.д.).

Дополнительно (для усложнения):

Добавьте возможность сохранять состояние библиотеки в файл и загружать его.
Реализуйте управление датами (например, чтобы книги можно было брать на ограниченный срок).
Добавьте учёт пользователей и сделайте возможным отслеживание, кто взял какую книгу.

Пример взаимодействия с библиотекой:

Добро пожаловать в библиотеку!
1. Показать доступные книги
2. Добавить книгу
3. Удалить книгу
4. Найти книги по автору
5. Взять книгу
6. Вернуть книгу
7. Выход
"""

import json
from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True  # Книга по умолчанию доступна
        self.borrowed_by = None  # Переменная для хранения информации о пользователе, который взял книгу
        self.due_date = None  # Дата возврата книги

    def borrow(self, user):
        # Проверка доступности книги для выдачи
        if self.is_available:
            self.is_available = False  # Меняем статус на "взята"
            self.borrowed_by = user  # Записываем, кто взял книгу
            self.due_date = datetime.now() + timedelta(days=14)  # Устанавливаем срок возврата через 14 дней
            return f"Книга '{self.title}' взята пользователем {user}. Дата возврата: {self.due_date.strftime('%Y-%m-%d')}"
        else:
            return f"Книга '{self.title}' уже взята пользователем {self.borrowed_by}. Дата возврата: {self.due_date.strftime('%Y-%m-%d')}"

    def return_book(self):
        # Проверка возврата книги
        if not self.is_available:
            self.is_available = True  # Меняем статус на "доступна"
            user = self.borrowed_by
            self.borrowed_by = None  # Очищаем информацию о пользователе
            self.due_date = None  # Очищаем дату возврата
            return f"Книга '{self.title}' возвращена пользователем {user}."
        return f"Книга '{self.title}' уже доступна."

    def get_full_info(self):
        # Получение полной информации о книге
        availability = "доступна" if self.is_available else f"взята, возвращена {self.due_date.strftime('%Y-%m-%d')}"
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, ISBN: {self.isbn}, Статус: {availability}"



# Класс Library не должен наследоваться от Books (Библиотека — это контейнер для книг, а не разновидность книги)
class Library:
    def __init__(self):
        self.books = []  # Инициализация пустого списка книг

    def add_book(self, book):
        # Добавление книги в библиотеку
        self.books.append(book)
        return f"Книга '{book.title}' добавлена в библиотеку."

    def remove_book(self, isbn):
        # Удаление книги из библиотеки по ISBN
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"Книга '{book.title}' удалена."
        return "Книга с таким ISBN не найдена."

    def find_books_by_author(self, author):
        # Поиск книг по автору
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            return "\n".join([f"{book.title} ({book.year})" for book in found_books])
        return "Книг этого автора не найдено."

    def list_available_books(self):
        # Список доступных книг
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            return "\n".join([f"{book.title} ({book.author}, {book.year}, ISBN: {book.isbn})" for book in available_books])
        return "Нет доступных книг."

    def borrow_book(self, isbn, user):
        # Выдача книги по ISBN
        for book in self.books:
            if book.isbn == isbn:
                return book.borrow(user)
        return "Книга с таким ISBN не найдена."

    def return_book(self, isbn):
        # Возврат книги по ISBN
        for book in self.books:
            if book.isbn == isbn:
                return book.return_book()
        return "Книга с таким ISBN не найдена."

    def save_to_file(self, filename="library.json"):
        # Сохранение библиотеки в файл
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def open_file(self, filename="library.json"):
        # Загрузка библиотеки из файла
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
                for data in books_data:
                    book = Book(**data)
                    self.books.append(book)
        except FileNotFoundError:
            print("Файл с данными библиотеки не найден.")

# Интерфейс для работы с библиотекой
def main():
    library = Library()

    # Добавляем книги в библиотеку
    library.add_book(Book("1984", "George Orwell", 1949, "12345"))
    library.add_book(Book("Brave New World", "Aldous Huxley", 1932, "67890"))
    library.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953, "11111"))

    while True:
        print("\nДобро пожаловать в библиотеку!")
        print("1. Показать доступные книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книги по автору")
        print("5. Взять книгу")
        print("6. Вернуть книгу")
        print("7. Выход")

        answer = input("Выберите действие: ")

        if answer == "1":
            print("\nДоступные книги:")
            print(library.list_available_books())

        elif answer == "2":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            isbn = input("Введите ISBN книги: ")
            print(library.add_book(Book(title, author, year, isbn)))

        elif answer == "3":
            isbn = input("Введите ISBN для удаления: ")
            print(library.remove_book(isbn))

        elif answer == "4":
            author = input("Введите имя автора: ")
            print("\nКниги автора:")
            print(library.find_books_by_author(author))

        elif answer == "5":
            isbn = input("Введите ISBN книги, которую хотите взять: ")
            user = input("Введите имя пользователя: ")
            print(library.borrow_book(isbn, user))

        elif answer == "6":
            isbn = input("Введите ISBN книги, которую хотите вернуть: ")
            print(library.return_book(isbn))

        elif answer == "7":
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()

