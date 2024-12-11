"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит в новый файл самое часто встречаемое слово в каждой строке
и число – счётчик количества повторений этого слова в строке.
"""

# Создаем функцию для нахождения самого частого слова в строке
def find_frequent_word(line):
    words = line.split()  #Разбиваем строку на слова и получаем список слов
    if not words:  #Если в строке нет слов, результат не выводится
        return None, 0

    # Создаем пустой словарь, где ключ - это слово, а значение - частота слова
    word_count = {}
    # Перебираем каждое слово в списке
    for word in words:
        # Ищем значение каждого ключа (слова) в словаре
        # Если ключа нет, создаем ключ и возвращаем значение 0
        # Если ключ есть, добавляем к нему значение +1
        word_count[word] = word_count.get(word, 0) + 1

        # Находим самое частое слово в строке
        most_frequent_word = max(word_count, key=word_count.get)
        count = word_count[most_frequent_word]

        # Возвращаем самое частое слово и количество использований
        return most_frequent_word, count


try:
    with open("text.txt", "r", encoding="utf-8") as text_file:
        # Цикл построчного чтения файла с нумерацией строк. Нумерацию начинаем с 1
        for line_number, line in enumerate(text_file, start=1):
            # Для каждой строки вызываем функцию find_most_frequent_word и получаем самое частое слово и его частоту
            most_frequent_word, count = find_frequent_word(line)
            # Выводим результат, если в строке есть слова. Если строка пустая, результат не выводится
            if most_frequent_word:
                print(f"Строка {line_number}: Самое частое слово - {most_frequent_word}, встречается {count} раз")


except FileNotFoundError:
    print("Файл не найден")

