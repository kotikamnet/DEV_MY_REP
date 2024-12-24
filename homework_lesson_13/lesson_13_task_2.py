"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2…).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся пользователем с клавиатуры.
"""

def numbers_generate(sequence):
    while True:
        for item in sequence:
            yield item

sequence = [1, 2, 3]
n = int(input("Введите количество чисел:"))

cycle = numbers_generate(sequence)

for _ in range(n):
    print(next(cycle), end=" ")
