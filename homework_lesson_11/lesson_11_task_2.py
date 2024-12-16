"""
Напишите программу с классом Math.
При инициализации атрибутов нет.
Реализовать методы addition, subtraction, multiplication и division.
При передаче в методы двух числовых параметров нужно производить с
параметрами соответствующие действия и печатать ответ.
"""

class Math:
    def addition(self, a, b):
        result = a + b
        return f"Сумма чисел: {result}"

    def subtraction(self, a, b):
        result = a - b
        return f"Разность чисел: {result}"

    def multiplication(self, a, b):
        result = a * b
        return f"Произведение чисел: {result}"

    def division(self, a, b):
        if b != 0:
            result = a / b
            return f"Деление чисел: {result}"

        else:
            return "На ноль делить нельзя"


a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))

# Методы класса Math нужно вызвать через объект этого класса - math_operations
# Методы addition, и т.д, являются методами экземпляра класса,
# то есть они требуют ссылки на конкретный объект, чтобы выполнять операции
math_actions = Math()


print(math_actions.addition(a, b))
print(math_actions.subtraction(a, b))
print(math_actions.multiplication(a, b))
print(math_actions.division(a, b))


