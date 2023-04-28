import time


class Auto:
    def __init__(self, age, brand, mark):
        self.age = age
        self.brand = brand
        self.color = 'blue'
        self.mark = mark
        self.weight = '1200kg'

    def move(self):
        return print("I'm moving")

    def stop(self):
        return print("I stopped")

    def birthday(self):
        self.age += 1
        return self.age

    def _technical_service(self):
        print('Service approved!')


big_auto = Auto(3, 'Toyota', 'Rav4S')


class Truck(Auto):
    def __init__(self, max_load, age, brand, mark):
        super().__init__(age, brand, mark)
        self.max_load = max_load

    def move(self):
        super()._technical_service()
        print('move')

    def load(self):
        time.sleep(1)
        print('Loading')
        time.sleep(1)


big_truck = Truck(3, 3,  'Reno', 'ddd')
big_truck.load()

class Car(Auto):
    def __init__(self, max_speed, age, brand, mark):
        super().__init__(age, brand, mark)
        self.max_speed = max_speed

    def move(self):
        print(f'Max speed is {self.max_speed}!~')
        super().move()


speedy_car = Car(90, 3, 'Tesla', 'ghd')
speedy_car.move()
