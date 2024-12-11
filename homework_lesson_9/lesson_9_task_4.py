"""
Напишите программу, которая получает на вход строку с названием текстового файла
и выводит на экран содержимое этого файла, заменяя все запрещённые слова звездочками.
"""

import re

# Функция для замены запрещённых слов на звездочки
def replace_words(text, stop_words):
    # Создаём регулярное выражение, которое ищет все запрещённые слова
    pattern = r"|".join(re.escape(word) for word in stop_words)
    # Заменяем все вхождения запрещённых слов звездочками
    replaced_text = re.sub(pattern, lambda match: "*" * len(match.group()), text, flags=re.IGNORECASE)
    return replaced_text

# Основная функция программы
def main():
    stopwords_file = "stop_words.txt"  # Имя файла с запрещёнными словами
    text_file = input("Введите имя файла: ")  # Имя файла с текстом для обработки

    try:
        # Чтение запрещённых слов
        with open(stopwords_file, "r", encoding="utf-8") as sw_file:
            stop_words = sw_file.read().split()  # Разбиваем слова по пробелам
    except FileNotFoundError:
        print("Файл с запрещенными словами не найден")
        return

    try:
        # Чтение текста для обработки
        with open(text_file, "r", encoding="utf-8") as t_file:
            original_text = t_file.read()
    except FileNotFoundError:
        print("Файл с текстом не найден")
        return

    # Замена запрещённых слов
    replaced_text = replace_words(original_text, stop_words)

    # Вывод результата
    print("\nЦензурированный текст:")
    print(replaced_text)

# Вызов основной функции
main()