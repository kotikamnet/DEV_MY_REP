"""
Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит два новых метода:

1. Метод is_repeatance(s), который принимает некоторую строку
и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым количеством повторов строки s.
Считать, что пустая строка не содержит повторов

2. Метод is_palindrom(), который возвращает True или False в зависимости от того,
является ли строка палиндромом вне зависимости от регистра.
Пустую строку считать палиндромом
"""

class SuperStr(str):

    def is_repeatance(self, s):
        if s == "" or len(self) % len(s) != 0:
            return False
        # Создаем строку, которая состоит из повторений s, и сравниваем с текущей строкой
        return self == s * (len(self) // len(s))


    def is_palindrom(self):
        return self.lower() == self[::-1].lower()

str_1 = SuperStr("Hello")

print(str_1.is_repeatance("hel"))
print(str_1.is_palindrom())

str_2 = SuperStr("xyzxyzxyz")

print(str_2.is_repeatance("xyz"))
print(str_2.is_palindrom())

str_3 = SuperStr("abccba")

print(str_3.is_repeatance("abc"))
print(str_3.is_palindrom())
