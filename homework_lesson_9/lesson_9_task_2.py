"""
Замена имён в судебном решении
Написать программу, которая заменит в тексте ФИО подсудимого на N.
Каждое слово в ФИО начинается с заглавной буквы, фамилия может быть двойная.
"""

import re

text = input("Введите текст:\n")

pattern = r"[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)? [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+"

new_text = re.sub(pattern, "N", text)

print(new_text)

