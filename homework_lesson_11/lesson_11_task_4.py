"""
Программа с классом Sphere для представления сферы в трёхмерном пространстве.
Реализовать методы:

1. Конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z.
Если конструктор вызывается без аргументов,
создать объект сферы с единичным радиусом и центром в начале координат.
Если конструктор вызывается только с радиусом,
создать объект с соответствующим радиусом и центром в начале координат

2. Метод get_volume(), возвращающий число – объем шара, ограниченного текущей сферой
3. Метод get_square(), возвращающий число – площадь внешней поверхности сферы
4. Метод get_radius(), возвращающий число – радиус текущей сферы
5. Метод get_center(), возвращающий кортеж с координатами центра сферы
6. Метод set_radius(radius), который принимает новое значение радиуса, меняет радиус текущей сферы и ничего не возвращает
7. Метод set_center(x, y, z), который принимает новые значения для координат центра радиуса,
меняет координаты текущей сферы и ничего не возвращает
8. Метод is_point_inside(x, y, z), который принимает координаты некой точки в трёхмерном пространстве и
возвращает True или False в зависимости от того, находится ли точка внутри сферы
"""

import math

class Sphere:
    # Конструктор, принимающий 4 числа: радиус и координаты центра сферы x, y, z.
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)


    def get_volume(self):
        return (4/3) * math.pi * self.radius**3

    def get_square(self):
        return 4 * math.pi * self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    # Метод для проверки, находится ли точка внутри сферы
    def is_point_inside(self, x, y, z):
            # Вычисляем расстояние от точки (x, y, z) до центра сферы
            distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
            return distance <= self.radius  # Точка внутри сферы, если расстояние меньше или равно радиусу

sphere = Sphere(3, 1, 2, 3)

point_inside = sphere.is_point_inside(1, 1, 1)  # Проверяем, внутри ли точка (1, 1, 1)

print(f"Объем сферы: {sphere.get_volume()}")
print(f"Площадь поверхности сферы: {sphere.get_square()}")
print(f"Радиус сферы: {sphere.get_radius()}")
print(f"Центр сферы: {sphere.get_center()}")
print(f"Точка внутри сферы: {point_inside}")




