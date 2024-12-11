"""
Реализовать функцию, которая выведет информацию об одном сотруднике по имени.
Имя для поиска вводится с клавиатуры
"""

import csv

def find_employee(csv_file):
    # Вводим имя сотрудника для поиска
    search_name = input("Введите имя сотрудника для поиска: ").strip()

    found = False  # Флаг, чтобы отслеживать, найден ли сотрудник

    # Открываем файл для чтения
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Пропускаем заголовки

        # Ищем сотрудника по имени
        for row in reader:
            name = row[0]  # Предполагаем, что имя в первом столбце
            if name.lower() == search_name.lower():
                print(f"Информация о сотруднике {search_name}:")
                print(f"Имя: {row[0]}")
                print(f"Дата рождения: {row[1]}")
                print(f"Рост: {row[2]} см")
                print(f"Вес: {row[3]} кг")
                print(f"Есть ли машина: {'Да' if row[4] == 'True' else 'Нет'}")
                print(f"Языки программирования: {', '.join(row[5].split(','))}")
                found = True
                break

    if not found:
        print(f"Сотрудник с именем {search_name} не найден.")

# Пример использования:
csv_file = "employees_new.csv"
find_employee(csv_file)