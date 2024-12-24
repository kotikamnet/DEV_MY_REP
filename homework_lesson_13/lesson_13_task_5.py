"""
 5. Паттерн «Стратегия»
 ● Создайте класс Calculator, который использует разные стратегии
для выполнения математических операций.

 ● Создайте несколько классов, каждый реализует определенную стратегию
математической операции, например, Addition, Subtraction, Multiplication, Division.
Каждый класс должен содержать метод execute,
который принимает два числа и выполняет соответствующую операцию.

 ● Calculator должен иметь метод set_strategy, который устанавливает текущую стратегию,
и метод calculate, который выполняет операцию с помощью текущей стратегии.
"""


"""
1 Вариант решения
"""

# Стратегия — это поведенческий паттерн проектирования, который определяет
# семейство схожих алгоритмов и помещает каждый из них в собственный класс,
# после чего алгоритмы можно взаимозаменять прямо во время исполнения программы.

class Calculator():
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        return self._strategy.execute(a, b)

class Addition():
    def execute(self, a, b):
        return a + b

class Subtraction():
    def execute(self, a, b):
        return a - b

class Multiplication():
    def execute(self, a, b):
        return a * b

class Division():
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b

calculator = Calculator()

calculator.set_strategy(Addition())
print("Сложение:", calculator.calculate(6, 5))

calculator.set_strategy(Subtraction())
print("Вычитание:", calculator.calculate(6, 5))

calculator.set_strategy(Multiplication())
print("Умножение:", calculator.calculate(6, 5))

calculator.set_strategy(Division())
print("Деление:", calculator.calculate(6, 5))


"""
2 Вариант решения через общий интерфейс всех стратегий - абстрактный класс Strategy
"""

from abc import ABC, abstractmethod

# Базовый класс Strategy
class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition1(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction1(Strategy):
    def execute(self, a, b):
        return a - b

class Multiplication1(Strategy):
    def execute(self, a, b):
        return a * b

class Division1(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно.")
        return a / b

class Calculator1:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if not self._strategy:
            raise ValueError("Стратегия не установлена!")
        return self._strategy.execute(a, b)


calculator1 = Calculator1()

calculator.set_strategy(Addition1())
print("Сложение:", calculator.calculate(6, 5))

calculator.set_strategy(Subtraction1())
print("Вычитание:", calculator.calculate(6, 5))

calculator.set_strategy(Multiplication1())
print("Умножение:", calculator.calculate(6, 5))

calculator.set_strategy(Division1())
print("Деление:", calculator.calculate(6, 5))