def calculate_index(weight, height):
    #Рассчитывает индекс массы тела
    return weight / (height ** 2)

def interpret_index(index):
    #Определяем категорию индекса массы тела
    if index < 18.5:
        return "Недостаточный вес"
    elif 18.5 <= index < 24.9:
        return "Нормальный вес"
    elif 25 <= index < 29.9:
        return "Избыточный вес"
    else:
        return "Ожирение"

def main():
    try:
        # Ввод данных
        weight = float(input("Введите ваш вес в килограммах: "))
        height = float(input("Введите ваш рост в метрах: "))

        # Проверяем, что данные правильные
        if weight <= 0 or height <= 0:
            raise ValueError("Вес и рост должны быть положительными числами.")

        # Расчёт индекса
        index = calculate_index(weight, height)

        # Вывод результата
        print(f"Ваш индекс массы тела: {index:.2f}")
        print(f"Классификация: {interpret_index(index)}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except ZeroDivisionError:
        print("Рост не может быть равен нулю.")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


main()
