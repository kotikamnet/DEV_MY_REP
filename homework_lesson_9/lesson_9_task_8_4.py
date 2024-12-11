

import csv

def add_employee_to_csv(csv_file):
    # Вводим данные о сотруднике
    print("Добавление нового сотрудника:")
    name = input("Введите имя сотрудника (Имя, Фамилия): ")
    birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
    height = int(input("Введите рост (в сантиметрах): "))
    weight = float(input("Введите вес (в килограммах): "))
    car = input("Есть ли машина? (да/нет): ").strip().lower() == "да"
    languages = input("Введите языки программирования (через запятую): ").split(",")

    # Формируем данные сотрудника
    employee = [name, birthday, height, weight, car, languages]

    # Проверяем, существует ли CSV файл
    file_exists = False
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            file_exists = True
    except FileNotFoundError:
        pass

    # Если файл существует, то добавляем данные, если нет, то создаем новый с заголовками
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        if not file_exists:
            # Записываем заголовки только если файл новый
            writer.writerow(['name', 'birthday', 'height', 'weight', 'car', 'languages'])

        writer.writerow(employee)

    print(f"Сотрудник {name} добавлен в файл {csv_file}.")

# Пример использования:
csv_file = "employees_new.csv"
add_employee_to_csv(csv_file)
