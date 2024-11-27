'''
Используя map() и reduce() посчитать площадь квартиры, имея на входе характеристики комнат квартиры.
'''

# Импортируем reduce, потому что эта функция не является частью стандартной библиотеки Python
from functools import reduce

# Вводим список с данными квартиры
rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]

# Вычисляем площадь каждой комнаты, умножаем длину на ширину
room_area = map(lambda room: room["length"] * room["width"], rooms)

# Складываем все элементы списка с помощью reduce
flat_area = reduce(lambda x, y: x + y, room_area)

# Выводим результат
print(f"Общая площадь квартиры: {flat_area} кв.м.")
