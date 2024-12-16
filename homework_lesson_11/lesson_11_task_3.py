"""
Программа с классом Car.
При инициализации объекта ему должны задаваться атрибуты color, type и year.
Реализовать пять методов.
Запуск автомобиля – выводит строку «Автомобиль заведён».
Отключение автомобиля – выводит строку «Автомобиль заглушен».
Методы для присвоения автомобилю года выпуска, типа и цвета.
"""


class Car:
    def __init__(self, color=None, type=None, year=None):
        self.color = color
        self.type = type
        self.year = year
        self.started_car = False

    def start_car(self):
        self.started_car = True
        return "Автомобиль заведен"

    def stop_car(self):
        self.started_car = False
        return "Автомобиль заглушен"

    def add_year(self, year):
        # Посоветовали хранить год как целое число
        self.year = int(year)
        return f"Год выпуска автомобиля установлен на {self.year}"

    def add_type(self, type):
        self.type = type
        return f"Тип автомобиля установлен на {self.type}"

    def add_color(self, color):
        self.color = color
        return f"Цвет автомобиля установлен на {self.color}"


car = Car()

print(car.add_color("синий"))
print(car.add_type("седан"))
print(car.add_year("2010"))

print(car.start_car())
print(car.stop_car())

print(vars(car))