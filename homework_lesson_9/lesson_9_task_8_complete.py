import json
import csv


# 1. Опция. Функция для чтения данных из JSON и переноса в CSV
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
        print("Данные успешно преобразованы из JSON в CSV.")
    except Exception as e:
        print(f"Ошибка: {e}")


# 2. Опция. Функция для сохранения данных в CSV
def save_to_csv(data, csv_file):
    try:
        with open(csv_file, "w", encoding="utf-8", newline="") as c_file:
            keys = data[0].keys()
            writer = csv.DictWriter(c_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print("Данные успешно сохранены в CSV.")
    except Exception as e:
        print(f"Ошибка: {e}")


# 3. Опция. Функция для добавления нового сотрудника в JSON
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
        print("Сотрудник успешно добавлен в JSON.")
    except Exception as e:
        print(f"Ошибка: {e}")


# 4. Опция. Функция для добавления нового сотрудника в CSV
def add_employee_to_csv(csv_file):
    try:
        # Вводим данные о сотруднике
        print("Добавление нового сотрудника:")
        name = input("Введите имя сотрудника (Имя, Фамилия): ")
        birthday = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        height = int(input("Введите рост (в сантиметрах): "))
        weight = float(input("Введите вес (в килограммах): "))
        car = input("Есть ли машина? (да/нет): ").strip().lower() == "да"
        languages = input("Введите языки программирования (через запятую): ").split(",")
        languages = [lang.strip() for lang in languages]  # Убираем лишние пробелы

        # Формируем данные сотрудника
        new_employee = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }

        # Записываем данные в CSV
        with open(csv_file, mode='a', encoding="utf-8", newline="") as c_file:
            writer = csv.DictWriter(c_file, fieldnames=new_employee.keys())
            writer.writerow(new_employee)
        print("Сотрудник успешно добавлен в CSV.")
    except Exception as e:
        print(f"Ошибка: {e}")


# 5. Опция. Функция для вывода информации о сотруднике по имени
def find_employee_by_name(data, name):
    for employee in data:
        if employee['name'].lower() == name.lower():
            return employee
    return None


# 6. Опция. Функция для фильтрации сотрудников по языку
def filter_by_language(data, language):
    result = [emp for emp in data if language.lower() in [lang.lower() for lang in emp['languages']]]
    return result


# 7. Опция. Функция для фильтрации по году рождения
def filter_by_year(data, year):
    filtered_employees = [emp for emp in data if int(emp['birthday'].split('.')[2]) < year]
    if filtered_employees:
        avg_height = sum(emp['height'] for emp in filtered_employees) / len(filtered_employees)
        return avg_height
    return None


# Главная функция с меню
def main():
    json_file = 'employees.json'
    csv_file = 'employees.csv'

    while True:
        print("\nВыберите действие:")
        print("1. Преобразовать JSON в CSV")
        print("2. Сохранить данные в CSV")
        print("3. Добавить сотрудника в JSON")
        print("4. Добавить сотрудника в CSV")
        print("5. Найти сотрудника по имени")
        print("6. Фильтр по языку программирования")
        print("7. Фильтр по году рождения (средний рост)")
        print("8. Выход")

        choice = input("Введите номер действия: ")

        try:
            with open(json_file, 'r', encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        if choice == '1':
            change_json_to_csv(json_file, csv_file)

        elif choice == '2':
            save_to_csv(data, csv_file)

        elif choice == '3':
            add_employee_to_json(json_file)

        elif choice == '4':
            add_employee_to_csv(csv_file)

        elif choice == '5':
            name = input("Введите имя сотрудника: ")
            employee = find_employee_by_name(data, name)
            if employee:
                print(employee)
            else:
                print("Сотрудник не найден.")

        elif choice == '6':
            language = input("Введите язык программирования: ")
            employees = filter_by_language(data, language)
            if employees:
                print("Сотрудники, владеющие этим языком программирования:")
                for emp in employees:
                    print(emp)
            else:
                print("Не найдено сотрудников с таким языком.")

        elif choice == '7':
            year = int(input("Введите год рождения: "))
            avg_height = filter_by_year(data, year)
            if avg_height is not None:
                print(f"Средний рост сотрудников, рожденных до {year}: {avg_height:.2f} см.")
            else:
                print("Нет сотрудников с таким годом рождения.")

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


main()
