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


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publication_year = Column(Integer, nullable=False)
    author = relationship('Author', back_populates='books')
    sales = relationship('Sale', back_populates='book')

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer, nullable=False)
    book = relationship('Book', back_populates='sales')

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_data():
    author1 = Author(first_name='Harper', last_name='Lee')
    author2 = Author(first_name='Leo', last_name='Tolstoy')
    author3 = Author(first_name='Herman', last_name='Melville')
    author4 = Author(first_name='George', last_name='Orwell')
    author5 = Author(first_name='F. Scott', last_name='Fitzgerald')

    session.add_all([author1, author2, author3, author4, author5])
    session.commit()

    book1 = Book(title='To Kill a Mockingbird', author_id=author1.id, publication_year=1960)
    book2 = Book(title='War and Peace', author_id=author2.id, publication_year=1869)
    book3 = Book(title='Moby Dick', author_id=author3.id, publication_year=1851)
    book4 = Book(title='1984', author_id=author4.id, publication_year=1949)
    book5 = Book(title='The Great Gatsby', author_id=author5.id, publication_year=1925)

    session.add_all([book1, book2, book3, book4, book5])
    session.commit()

    sale1 = Sale(book_id=book1.id, quantity=5)
    sale2 = Sale(book_id=book2.id, quantity=7)
    sale3 = Sale(book_id=book3.id, quantity=13)
    sale4 = Sale(book_id=book4.id, quantity=0)
    sale5 = Sale(book_id=book5.id, quantity=9)

    session.add_all([sale1, sale2, sale3, sale4, sale5])
    session.commit()

add_data()
