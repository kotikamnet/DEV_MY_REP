"""
Создайте класс Soda (газировка).
Для инициализации есть параметр, который определяет вкус газировки.
При инициализации этот параметр можно задавать, а можно и не задавать.
Реализовать метод строковой репрезентации, который возвращает строку вроде
«У вас газировка с <клубничным> вкусом», если вкус задан.
Если вкус не задан, метод должен возвращать строку «У вас обычная газировка».
"""

class Soda:
    def __init__(self, taste=None):
        self.taste = taste

# Метод строковой репрезентации. __str__ предназначен для создания удобочитаемого описания объекта.
# Вызывается функцией str() и оператором print. (есть две функции: __str__ и __repr__)
    def __str__(self):
        if self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        else:
            return "У вас обычная газировка"


a = Soda("клубничным")
print(a)

b = Soda()
print(b)
