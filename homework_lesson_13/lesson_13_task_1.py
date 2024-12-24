"""
Реализовать программу для вывода последовательности чисел Фибоначчи
до определённого числа в последовательности.
Номер числа, до которого нужно выводить, задаётся пользователем с клавиатуры.
Для реализации последовательности использовать генераторную функцию.
"""
def fib_generate(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Ввод от пользователя
n = int(input("Введите номер числа Фибоначчи, до которого нужно вывести последовательность: "))

# Вывод последовательности
for fib_number in fib_generate(n):
    print(fib_number)
