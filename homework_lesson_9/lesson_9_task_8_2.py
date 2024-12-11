"""
2. Реализовать функцию, которая сохранит данные в CSV-файл
"""

import csv

def add_person_to_csv(csv_file):
    try:
        new_person = {
            "name": "Vasya Pupkin",
            "birthday": "15.03.1995",
            "height": 180,
            "weight": 75.2,
            "car": False,
            "languages": "Python, JavaScript"
        }
        # Открываем CSV-файл в режиме добавления
        with open(csv_file, "a", encoding="utf-8", newline="") as c_file:
            headers = ["name", "birthday", "height", "weight", "car", "languages"]
            writer = csv.DictWriter(c_file, fieldnames=headers)

            # Добавляем нового человека
            writer.writerow(new_person)

        print(f"Новый человек ({new_person['name']}) успешно добавлен в файл {csv_file}.")
    except Exception as e:
        print(f"Ошибка: {e}")

# Пример вызова
csv_file = "employees.csv"
add_person_to_csv(csv_file)