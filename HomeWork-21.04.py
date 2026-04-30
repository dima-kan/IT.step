# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує


class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        if self.speed <= 0:
            print("Помилка: Швидкість має бути більшою за 0!")
            return
        time = distance / self.speed

        print(f"Транспорт рухається до {destination}.")
        print(f"Відстань: {distance} км, швидкість: {self.speed} км/год")
        print(f"Час у дорозі: {time:.2f} годин")


# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()


class Bus(Transport):
    def __init__(self, speed, capacity, passengers=None):
        super().__init__(speed)

        self.capacity = capacity

        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} сів в автобус.")
        else:
            print(f"Автобус переповнений. Пасажир {passenger.name} не зміг сісти.")

    def move(self, destination, distance):
        total = 0

        for passenger in self.passengers:
            if passenger.destination == destination:
                total += 1
        print(f"Висаджуємо {total} пасажирів у {destination}")

        new_passengers = []

        for p in self.passengers:
            if p.destination != destination:
                new_passengers.append(p)

        self.passengers = new_passengers

        super().move(destination, distance)
