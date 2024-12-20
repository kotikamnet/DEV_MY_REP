class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passengers = []  # Список пассажиров
        self.seats_dict = {i: None for i in range(1, max_seats + 1)}  # Словарь мест
        self.free_seats = True  # Флаг наличия свободных мест

    def add_passenger(self, *passenger_names):
        """Посадка одного или нескольких пассажиров"""
        for name in passenger_names:
            if len(self.passengers) < self.max_seats:
                self.passengers.append(name)
                # Находим первое свободное место
                for seat, passenger in self.seats_dict.items():
                    if passenger is None:
                        self.seats_dict[seat] = name
                        break
            else:
                print(f"Мест нет. Пассажир {name} не может сесть.")

        # Обновляем флаг свободных мест
        self.free_seats = len(self.passengers) < self.max_seats

    def remove_passenger(self, *passenger_names):
        """Высадка одного или нескольких пассажиров"""
        for name in passenger_names:
            if name in self.passengers:
                self.passengers.remove(name)
                # Освобождаем место
                for seat, passenger in self.seats_dict.items():
                    if passenger == name:
                        self.seats_dict[seat] = None
                        break
            else:
                print(f"Пассажир {name} не найден в списке.")

        # Обновляем флаг свободных мест
        self.free_seats = len(self.passengers) < self.max_seats

    def increase_speed(self, incr_value):
        """Увеличение скорости на заданное значение"""
        if self.speed + incr_value <= self.max_speed:
            self.speed += incr_value
        else:
            print(f"Скорость не может быть больше максимальной ({self.max_speed}).")

    def decrease_speed(self, decr_value):
        """Уменьшение скорости на заданное значение"""
        if self.speed - decr_value >= 0:
            self.speed -= decr_value
        else:
            print("Скорость не может быть меньше 0.")

    def __contains__(self, passenger_name):
        """Операция in для проверки наличия пассажира в автобусе"""
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        """Операция += для посадки пассажира"""
        self.add_passenger(passenger_name)
        return self

    def __isub__(self, passenger_name):
        """Операция -= для высадки пассажира"""
        self.remove_passenger(passenger_name)
        return self

    def __str__(self):
        return (f"Скорость: {self.speed} км/ч\n"
                f"Пассажиров: {len(self.passengers)} / {self.max_seats}\n"
                f"Свободные места: {self.free_seats}\n"
                f"Места: {self.seats_dict}")


# Пример использования
bus = Bus(max_seats=3, max_speed=100)

# Посадка пассажиров
bus.add_passenger("Иванов", "Петров")
print(bus)

# Проверка наличия пассажира
print("Иванов в автобусе?", "Иванов" in bus)

# Посадка нового пассажира
bus += "Сидоров"
print(bus)

# Увеличение скорости
bus.increase_speed(30)
print(bus)

# Высадка пассажира
bus -= "Петров"
print(bus)

# Уменьшение скорости
bus.decrease_speed(10)
print(bus)
