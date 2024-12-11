"""
Реализовать функцию фильтра по языку: с клавиатуры вводится язык программирования,
выводится список всех сотрудников, кто владеет этим языком программирования.
"""

import csv


def find_employee_by_language(csv_file):
    # Вводим язык программирования
    language = input("Введите язык программирования: ").strip().lower()

    found = False  # Флаг, чтобы отслеживать, найден ли хотя бы один сотрудник

    # Открываем файл для чтения
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Пропускаем заголовки

        print(f"Сотрудники, владеющие языком {language}:")

        # Ищем сотрудников, владеющих этим языком
        for row in reader:
            languages = [lang.strip().lower() for lang in row[5].split(',')]  # Языки в столбце 5
            if language in languages:
                print(f"Имя: {row[0]}")
                print(f"Дата рождения: {row[1]}")
                print(f"Рост: {row[2]} см")
                print(f"Вес: {row[3]} кг")
                print(f"Есть ли машина: {'Да' if row[4] == 'True' else 'Нет'}")
                print(f"Языки программирования: {', '.join(languages)}\n")
                found = True

    if not found:
        print(f"Нет сотрудников, владеющих языком {language}.")


# Пример использования:
csv_file = "employees_new.csv"
find_employee_by_language(csv_file)