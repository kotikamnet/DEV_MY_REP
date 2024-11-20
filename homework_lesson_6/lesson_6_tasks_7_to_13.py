"""
Задание 7. Реализовать функцию, которая создаёт матрицу размером
M строк на N столбцов и заполняет её рандомными числами.
"""

import random


# Задание 7: Функция для создания матрицы
def create_matrix(rows, columns):
    matrix_content = []  # Пустой список для хранения строк матрицы
    for i in range(rows):
        row = []  # Создаём новую строку
        for _ in range(columns):
            row.append(random.randint(1, 100))  # Добавляем случайное число от 1 до 100
        matrix_content.append(row)  # Добавляем строку в матрицу
    return matrix_content  # Возвращаем значение


# Вводим количество строк и столбцов
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))

# Создаём матрицу
result_matrix = create_matrix(m, n)

# Выводим матрицу
print("\nСгенерированная матрица:")
for row in result_matrix:
    print(row)

"""
Задание 8. Реализовать функцию, которая находит минимальный и максимальный элементы в матрице.
Вывести в консоль индексы найденных элементов.
"""


def find_min_max(matrix):
    min_value = float('inf')  # Минимальное значение (начально бесконечность)
    max_value = float('-inf')  # Максимальное значение (начально минус бесконечность)
    min_index = (-1, -1)  # Индексы минимального элемента
    max_index = (-1, -1)  # Индексы максимального элемента

    for i in range(len(matrix)):  # Проходим по строкам
        for j in range(len(matrix[i])):  # Проходим по элементам строки
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_index = (i, j)  # Сохраняем индексы минимального элемента
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_index = (i, j)  # Сохраняем индексы максимального элемента

    return min_value, min_index, max_value, max_index


# Находим минимальный и максимальный элементы
min_val, min_pos, max_val, max_pos = find_min_max(result_matrix)

# Выводим результаты
print(f"\nМинимальный элемент: {min_val}, его индексы: {min_pos}")
print(f"Максимальный элемент: {max_val}, его индексы: {max_pos}")

"""
Задание 9.  Реализовать функцию, которая находит сумму элементов матрицы.
Определить, какую долю в общей сумме (процент) составляет сумма элементов каждого столбца.
"""


def calculate_column_percentage(matrix):
    total_sum = 0  # Общая сумма всех элементов матрицы
    column_sums = [0] * len(matrix[0])  # Список для хранения суммы каждого столбца

    # Считаем суммы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total_sum += matrix[i][j]  # Суммируем общий элемент
            column_sums[j] += matrix[i][j]  # Добавляем элемент в сумму столбца

    # Рассчитываем проценты
    column_percentages = [(col_sum / total_sum) * 100 for col_sum in column_sums]

    return total_sum, column_sums, column_percentages


# Вызываем функцию и выводим результаты
total, column_sums, percentages = calculate_column_percentage(result_matrix)

print(f"\nОбщая сумма элементов матрицы: {total}")
for i, (col_sum, percentage) in enumerate(zip(column_sums, percentages), start=1):
    print(f"Сумма элементов столбца {i}: {col_sum} ({percentage:.2f}%)")

"""
Задание 12. Программа получает на вход число H. Реализовать функцию, 
которая определяет, какие столбцы имеют хотя бы одно такое же число, а какие не имеют. 
"""


def find_columns_with_number(matrix, h):
    columns_with_h = set()  # Множество для хранения индексов столбцов с числом h
    columns_without_h = set(range(len(matrix[0])))  # Все индексы столбцов

    # Проверяем каждую ячейку матрицы
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == h:
                columns_with_h.add(j)  # Добавляем столбец с h

    # Находим столбцы, в которых нет числа H
    columns_without_h -= columns_with_h

    return sorted(columns_with_h), sorted(columns_without_h)


# Вводим число h
h = int(input("\nВведите число H (для задания 12): "))

# Вызываем функцию и выводим результаты
cols_with_h, cols_without_h = find_columns_with_number(result_matrix, h)

# Выводим результат
if cols_with_h:
    print(f"Число {h} есть в следующих столбцах: {', '.join(map(str, [col + 1 for col in cols_with_h]))}")
else:
    print(f"Число {h} отсутствует во всех столбцах.")

if cols_without_h:
    print(f"Число {h} отсутствует в следующих столбцах: {', '.join(map(str, [col + 1 for col in cols_without_h]))}")
else:
    print(f"Число {h} есть во всех столбцах.")

"""
Задание 13. Реализовать функцию, которая находит сумму элементов 
на главной диагонали и сумму элементов на побочной диагонали
"""


def calculate_diagonal_sums(matrix):
    main_diagonal_sum = 0  # Сумма главной диагонали
    secondary_diagonal_sum = 0  # Сумма побочной диагонали
    n = len(matrix)  # Предполагается, что матрица квадратная

    for i in range(n):
        main_diagonal_sum += matrix[i][i]  # Элемент главной диагонали
        secondary_diagonal_sum += matrix[i][n - i - 1]  # Элемент побочной диагонали

    return main_diagonal_sum, secondary_diagonal_sum


# Вызов функции и вывод результатов
main_sum, secondary_sum = calculate_diagonal_sums(result_matrix)

print(f"\nСумма элементов главной диагонали: {main_sum}")
print(f"Сумма элементов побочной диагонали: {secondary_sum}")
