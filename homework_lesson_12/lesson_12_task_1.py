"""
Класс «Товар» содержит следующие закрытые поля:
 ● название товара
 ● название магазина, в котором подаётся товар
 ● стоимость товара в рублях

Класс «Склад» содержит закрытый массив товаров.
Обеспечить следующие возможности:
 ● вывод информации о товаре со склада по индексу
 ● вывод информации о товаре со склада по имени товара
 ● сортировка товаров по названию, по магазину и по цене
 ● перегруженная операция сложения товаров по цене
 """

# Класс Товары
class Goods:
    def __init__(self, name, shop, cost):
        # Закрытые поля обозначаются двумя подчеркиваниями __ в начале
        self.__name = name
        self.__shop = shop
        self.__cost = cost

    # Геттеры для доступа к закрытым полям
    def get_name(self):
        return self.__name

    def get_shop(self):
        return self.__shop

    def get_cost(self):
        return  self.__cost

    def get_full_info(self):
        return f"Название {self.__name}, Магазин {self.__shop}, Цена {self.__cost} рублей"



# Класс Склад
class Warehouse:
    def __init__(self):
        self.__goods = [] #Закрытый массив

    def add_goods(self, goods):
        self.__goods.append(goods)


    def get_info_with_index(self, index):
        if 0 <= index < len(self.__goods):
            return self.__goods[index].get_full_info()
        return "Товар с таким индексом не найден."

    def get_info_with_name(self, name):
        for goods in self.__goods:
            if goods.get_name() == name:
                return goods.get_full_info()
        return "Товар с таким названием не найден"

    # Cортировка товаров по названию, по магазину и по цене
    def sort_with_price(self):
        self.__goods.sort(key=lambda goods: goods.get_cost())

    def sort_with_shop(self):
        self.__goods.sort(key=lambda goods: goods.get_shop())

    def sort_with_cost(self):
        self.__goods.sort(key=lambda goods: goods.get_cost())

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total_cost = sum(goods.get_cost() for goods in self.__goods) + \
                         sum(goods.get_cost() for goods in other.__goods)
            return total_cost
        return NotImplemented

    def list_goods(self):
        return "\n".join(goods.get_full_info() for goods in self.__goods) if self.__goods else "Склад пуст"

def main():
    goods1 = Goods("Телевизор", "Электроника", 30000)
    goods2 = Goods("Смартфон", "Мобильный магазин", 20000)
    goods3 = Goods("Ноутбук", "Компьютерный магазин", 50000)
    goods4 = Goods("Пылесос", "Электроника", 10000)

    warehouse1 = Warehouse()
    warehouse2 = Warehouse()

    warehouse1.add_goods(goods1)
    warehouse1.add_goods(goods2)

    warehouse2.add_goods(goods3)
    warehouse2.add_goods(goods4)

    print("Товары на складе 1:")
    print(warehouse1.list_goods())

    print("Товары на складе 2:")
    print(warehouse2.list_goods())

#  ● вывод информации о товаре со склада по индексу

    print("Информация о товаре по индексу 1 (склад 1)")
    print(warehouse1.get_info_with_index(1))

    print("Информация о товаре по индексу 1 (склад 2)")
    print(warehouse2.get_info_with_index(1))

#  ● вывод информации о товаре со склада по имени товара

    print("Информация о товаре под названием 'Ноутбук':")
    print(warehouse2.get_info_with_name("Ноутбук"))

# ● сортировка товаров по названию, по магазину и по цене

    print("Сортировка товаров на складе 1 по цене")
    warehouse1.sort_with_cost()
    print(warehouse1.list_goods())

    print("Сортировка товаров на складе 2 по цене")
    warehouse2.sort_with_cost()
    print(warehouse2.list_goods())


 # ● перегруженная операция сложения товаров по цене

    print("Суммарная стоимость товаров на складах")
    print(warehouse1 + warehouse2)

if __name__ == '__main__':
    main()
