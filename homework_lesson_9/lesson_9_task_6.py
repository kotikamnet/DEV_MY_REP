"""
В файл записано некоторое содержимое (буквы, цифры, пробелы, специальные символы и т.д.).
Числом назовём последовательность цифр, идущих подряд.
Вывести сумму всех чисел, записанных в файле.
"""


import re


def sum_numbers(digits_file):
    try:
        # Открываем файл для чтения
        with open(digits_file, "r", encoding="utf-8") as d_file:
            content = d_file.read()  # Читаем содержимое файла

        # Ищем все числовые последовательности в тексте
        numbers = re.findall(r"\d+", content)  # \d+ ищет последовательности цифр

        # Преобразуем числа в int и считаем их сумму
        numbers_sum = sum(int(num) for num in numbers)

        # Выводим результат
        print(f"Сумма всех чисел в файле: {numbers_sum}")

    except FileNotFoundError:
        # Обработка ошибки отсутствия файла
        print("Файл не найден. Убедитесь, что имя файла указано правильно.")


# Пример вызова функции
digits_file = "digits.txt"
sum_numbers(digits_file)