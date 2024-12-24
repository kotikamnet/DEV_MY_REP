"""
Задача: Реализуйте генератор, который построчно считывает текстовый файл (ленивое чтение).

Напишите функцию file_reader(file_path), которая возвращает строки файла по одной.
Не загружайте весь файл в память.

Пример использования:
for line in file_reader("example.txt"):
    print(line.strip())

Дополнительно: Реализуйте генератор, который возвращает только строки, содержащие слово "Python".
"""

def file_reader(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line


def python_lines(file_path):
    for line in file_reader(file_path):
        if "Python" in line:
            yield line