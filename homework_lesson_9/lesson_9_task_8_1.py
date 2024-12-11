"""
 JSON и CSV.
"""


import json
import csv

"""
1. Реализовать функцию, которая считает данные из исходного JSON-файла и преобразует их в формат CSV 
"""
def change_json_to_csv(json_file, csv_file):
    try:
        # Читаем данные из JSON-файла
        with open(json_file, "r", encoding="utf-8") as j_file:
            data = json.load(j_file)

        if not data:
            print("JSON-файл пуст")
            return

        # Записываем данные в CSV-файл
        keys = data[0].keys()  # Получаем заголовки из ключей первого словаря
        with open(csv_file, "w", encoding="utf-8", newline="") as c_file:
            writer = csv.DictWriter(c_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"Данные успешно скопированы из {json_file} в {csv_file}.")
    except FileNotFoundError:
        print("JSON-файл не найден!")
    except Exception as e:
        print(f"Ошибка: {e}")

json_file = "employees.json"
csv_file = "employees.csv"

change_json_to_csv(json_file, csv_file)

