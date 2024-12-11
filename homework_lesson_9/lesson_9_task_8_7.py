"""
Реализовать функцию фильтра по году: ввести с клавиатуры год рождения,
вывести средний рост всех сотрудников, у которых год рождения меньше заданного.
"""

import csv

def filter_and_calculate_height (csv_file):
    # Вводим год рождения для фильтрации
    year = int(input("Введите год рождения для фильтрации: "))

    total_height = 0  # Сумма роста
    count = 0  # Количество сотрудников, которые соответствуют фильтру

    # Открываем CSV файл для чтения
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Пропускаем заголовки

        for row in reader:
            birth_year = int(row[1].split('.')[-1])  # Извлекаем год рождения из даты (предположим формат ДД.ММ.ГГГГ)
            if birth_year < year:
                total_height += int(row[2])  # Предполагаем, что рост в 3-й колонке
                count += 1

    if count > 0:
        average_height = total_height / count
        print(f"Средний рост сотрудников, чьи годы рождения меньше {year}: {average_height:.2f} см.")
    else:
        print(f"Нет сотрудников, чей год рождения меньше {year}.")

# Пример использования:
csv_file = "employees_new.csv"
filter_and_calculate_height(csv_file)