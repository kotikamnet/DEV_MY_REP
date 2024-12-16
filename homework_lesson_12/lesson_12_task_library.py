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

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return f"Книга '{self.title}' успешно взята."
        return f"Книга '{self.title}' уже занята."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return f"Книга '{self.title}' возвращена и доступна."
        return f"Книга '{self.title}' уже доступна."


# Класс Library не должен наследоваться от Books (Библиотека — это контейнер для книг, а не разновидность книги)
class Library:
    def __init__(self):
        self.books = []  # Инициализация пустого списка книг

    def add_book(self, book):
        self.books.append(book)
        return f"Книга '{book.title}' добавлена в библиотеку."

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"Книга '{book.title}' удалена."
        return "Книга с таким ISBN не найдена."

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            return "\n".join([f"{book.title} ({book.year})" for book in found_books])
        return "Книг этого автора не найдено."

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            return "\n".join(
                [f"{book.title} ({book.author}, {book.year}, ISBN: {book.isbn})" for book in available_books]
            )
        return "Нет доступных книг."

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.borrow()
        return "Книга с таким ISBN не найдена."

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book.return_book()
        return "Книга с таким ISBN не найдена."

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
            print(library.borrow_book(isbn))

        elif answer == "6":
            isbn = input("Введите ISBN книги, которую хотите вернуть: ")
            print(library.return_book(isbn))

        elif answer == "7":
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")


main()
