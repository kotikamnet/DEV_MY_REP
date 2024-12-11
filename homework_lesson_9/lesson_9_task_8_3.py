"""
Реализовать функцию, которая добавит информацию о новом сотруднике в JSON-файл.
Пошагово вводятся все необходимые данные о сотруднике, формируются данные для записи.
"""

import json

def add_employee_to_json(json_file):
    try:
        # Считываем данные из файла
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)  # Загружаем текущие данные
        except FileNotFoundError:
            data = []  # Если файл не существует, создаём новый список

        # Ввод данных нового сотрудника
        print("Добавление нового сотрудника:")
        name = input("Введите имя сотрудника (Имя, Фамилия): ")
        birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        height = int(input("Введите рост (в сантиметрах): "))
        weight = float(input("Введите вес (в килограммах): "))
        car = input("Есть ли машина? (да/нет): ").strip().lower() == "да"
        languages = input("Введите языки программирования (через запятую): ").split(",")
        languages = [lang.strip() for lang in languages]  # Убираем лишние пробелы

        # Формируем данные нового сотрудника
        new_employee = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }

        # Добавляем нового сотрудника к данным
        data.append(new_employee)

        # Записываем обновлённые данные обратно в файл
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Сотрудник {name} успешно добавлен в файл {json_file}.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример вызова функции
json_file = "employees_new.json"
add_employee_to_json(json_file)
