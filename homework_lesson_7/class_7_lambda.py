"""
Создать 2 переменные.
В них через анонимную функцию передается по 3 значения. В одной все значения складываются, в другой все отнимаются.
Значения могут быть на ваш вкус, но после всех расчетов значения нужно сумму значений вывести в принте.
"""

# Анонимная функция для сложения
add_numbers = lambda x, y, z: x + y + z

# Анонимная функция для вычитания
subtract_numbers = lambda x, y, z: x - y - z

# Ввод значений
a, b, c = 5, 10, 15

# Считаем сумму и разность
add_result = add_numbers(a, b, c)
substract_result = subtract_numbers(a, b, c)

# Выводим результаты
print(f"Сумма значений: {add_result}")
print(f"Разность значений: {substract_result}")
