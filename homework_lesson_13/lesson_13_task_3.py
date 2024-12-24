"""
3. Паттерн «Строитель»
 ● Создайте класс Pizza, который содержит следующие атрибуты:
 size, cheese, pepperoni, mushrooms, onions, bacon.

 ● Создайте класс PizzaBuilder, который использует паттерн «Строитель» для создания экземпляра Pizza.
Этот класс должен содержать методы для добавления каждого из атрибутов Pizza.

 ● Создайте класс PizzaDirector, который принимает экземпляр PizzaBuilder и содержит метод make_pizza,
который использует PizzaBuilder для создания Pizza.
"""

# Строитель — это порождающий паттерн проектирования,
# который позволяет создавать сложные объекты пошагово.
# Строитель даёт возможность использовать один и тот же
# код строительства для получения разных представлений объектов.

class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    # Метод __str__ для форматирования информации о пицце в удобочитаемый строковый вид.
    # Когда мы пытаемся вывести объект Pizza с помощью функции print или
    #преобразовать его в строку через str(), Python автоматически вызывает этот метод.
    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("Cheese")
        if self.pepperoni: toppings.append("Pepperoni")
        if self.mushrooms: toppings.append("Mushrooms")
        if self.onions: toppings.append("Onions")
        if self.bacon: toppings.append("Bacon")
        toppings_str = ", ".join(toppings) if toppings else "None"
        return f"Pizza (size: {self.size}, toppings: {toppings_str})"


# Паттерн Строитель предлагает вынести конструирование объекта
# за пределы его собственного класса, поручив это дело отдельным объектам,
# которые следует называть строителями.

# Паттерн предлагает разбить процесс конструирования объекта на отдельные шаги.
# Чтобы создать объект, вам нужно поочерёдно вызывать методы строителя.
# Причём не нужно запускать все шаги, а только те, что нужны для производства объекта определённой конфигурации.

class PizzaBuilder:
    def __init__(self):
        self._pizza = None

    def set_size(self, size):
        self._pizza = Pizza(size=size)
        return self

    def add_cheese(self):
        self._pizza.cheese = True
        return self

    def add_pepperoni(self):
        self._pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self._pizza.mushrooms = True
        return self

    def add_onions(self):
        self._pizza.onions = True
        return self

    def add_bacon(self):
        self._pizza.bacon = True
        return self

    def build(self):
        return self._pizza

# Можно пойти дальше и выделить вызовы методов строителя в отдельный класс, называемый директором.
# В этом случае директор будет задавать порядок шагов строительства, а строитель — выполнять их.

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self._builder = builder

    def make_pizza(self):
        return (self._builder
                .set_size("Large")
                .add_cheese()
                .add_pepperoni()
                .add_mushrooms()
                .add_onions()
                .add_bacon()
                .build())


builder = PizzaBuilder()
director = PizzaDirector(builder)

# Используем директора для создания пиццы
pizza1 = director.make_pizza()
print(pizza1)  # Pizza (size: Large, toppings: Cheese, Pepperoni, Bacon)

# Используем билдера для создания пиццы вручную
pizza2 = (builder
          .set_size("Medium")
          .add_cheese()
          .add_mushrooms()
          .build())
print(pizza2)
