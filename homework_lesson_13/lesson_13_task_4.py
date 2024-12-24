"""
 4. Паттерн «Фабричный метод»
 ● Создайте абстрактный класс Animal, у которого есть абстрактный метод speak.
 ● Создайте классы Dog и Cat, которые наследуют от Animal и реализуют метод speak.
 ● Создайте класс AnimalFactory, который использует паттерн «Фабричный метод» для создания экземпляра Animal.
Этот класс должен иметь метод create_animal, который принимает строку («dog» или «cat»)
и возвращает соответствующий объект (Dog или Cat)
"""

# abc.ABC – базовый класс для создания абстрактных классов.
# Абстрактный класс содержит один или несколько абстрактных методов,
# то есть методов без определения (пустых, без кода).
# Эти методы необходимо переопределить в подклассах.

# Определить абстрактный класс возможно при помощи специализированного модуля abc и декоратора @abstractmethod

from abc import ABC, abstractmethod

# Фабричный метод — это порождающий паттерн проектирования,
# который определяет общий интерфейс для создания объектов в суперклассе,
# позволяя подклассам изменять тип создаваемых объектов

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return "Мяу"

class AnimalFactory():
    # Используется статический метод @staticmethod, так как фабрика не требует состояния объекта.
    @staticmethod
    def create_animal(animal_type: str):
        if animal_type.lower() == "dog":
            return Dog()

        elif animal_type.lower() == "cat":
            return Cat()

        else:
            raise ValueError(f"Неизвестное животное, должно быть: cat или dog")

factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())

cat = factory.create_animal("cat")
print(cat.speak())

# проверяем на ложное значение
mouse = factory.create_animal("mouse")
print(mouse.speak())
