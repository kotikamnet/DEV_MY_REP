"""
В текстовый файл построчно записаны фамилия и имя учащихся класса и оценка за контрольную.
Вывести на экран всех учащихся, чья оценка меньше трёх баллов
"""

def find_low_grades(students_file):
    try:
        with open(students_file, "r", encoding="utf-8") as file:
            print("Учащиеся с оценками меньше 3:")
            for line in file:
                data = line.split()  # Разделяем строку на части
                if len(data) < 3:
                    continue  # Пропускаем строки с недостатком данных

                surname, name, grade = data[0], data[1], data[2]  # Извлекаем фамилию, имя и оценку

                if grade.isdigit() and int(grade) < 3:  # Проверяем, является ли оценка числом и меньше ли 3
                    print(f"{surname} {name} - оценка {grade}")  # Выводим результат
    except FileNotFoundError:
        print("Файл не найден. Проверьте имя файла.")


# Пример вызова функции
students_file = "students.txt"
find_low_grades(students_file)