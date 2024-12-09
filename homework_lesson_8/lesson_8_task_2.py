def calculator():

    try:
        # Ввод чисел и операции
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, *, /): ").strip()

        # Выполнение операции
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            result = num1 / num2
        else:
            raise ValueError("Некорректная операция. Выберите одну из: +, -, *, /.")

        print(f"Результат: {result}")

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except ZeroDivisionError as zde:
        print(f"Ошибка: {zde}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

calculator()
