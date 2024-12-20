"""
 2. ПчёлоСлон
 Экземпляр класса инициализируется двумя целыми числами,
первое относится к пчеле, второе – к слону.

Класс реализует следующие методы:
  ● fly() – возвращает True, если часть пчелы не меньше части слона, иначе – False
  ● trumpet() – если часть слона не меньше части пчелы, возвращает строку “tu-tu-doo-doo”, иначе – “wzzzz”
  ● eat(meal, value) – может принимать в meal только ”nectar” или “grass”.
    Если съедает нектар, то value вычитается из части слона, пчеле добавляется. Иначе – наоборот.
    Не может увеличиваться больше 100 и уменьшаться меньше 0.
"""

class BeeElefant:
     def __init__(self, a, b):
          self.a = max(0, min(100, int(a)))
          self.b = max(0, min(100, int(b)))

     def fly(self):
          return self.a >= self.b


     def trumpet(self):
          if self.a <= self.b:
               return "tu-tu-doo-doo"
          else:
               return "wzzzz"

     def eat(self, meal, value):
          # дополнительно проверим на вводимое значение
          if meal not in ("nectar", "grass"):
               raise ValueError("meal должен быть 'nectar' или 'grass'.")

          if meal == "nectar":
               self.a = max(0, min(100, self.a + value))
               self.b = max(0, min(100, self.b - value))

          if meal == "grass":
               self.a = max(0, min(100, self.a - value))
               self.b = max(0, min(100, self.b + value))


exemplar = BeeElefant(3, 4)

print(exemplar.fly())
print(exemplar.trumpet())

exemplar.eat("nectar", 5)
print(exemplar.a, exemplar.b)

print(exemplar.a, exemplar.b)
exemplar.eat("grass", 7)



