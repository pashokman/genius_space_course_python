"""
**Завдання 1: Наслідування**

Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
- `make` (виробник)
- `model` (модель)
- `year` (рік виробництва)
Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. 
Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. 
Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.

Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.
"""


class Vehicle:

    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year


class Car(Vehicle):

    def __init__(self, make, model, year, fuel_type:str):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Engine is running.")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, speeds:int, mod_exhaust:bool):
        super().__init__(make, model, year)
        self.speeds = speeds
        self.mod_exhaust = mod_exhaust

    def fastest(self):
        print("This transport is the fastest.")

    def info(self):
        print(self.__dict__)


class Bicycle(Vehicle):

    def __init__(self, make, model, year, wheel_radius:int, seats_count:int):
        super().__init__(make, model, year)
        self.wheel_radius = wheel_radius
        self.seats_count = seats_count

    def info(self):
        print(f"Bicycle manifacturer: {self.make}, model: {self.model}, year: {self.year}, wheel radius: {self.wheel_radius}, seats count: {self.seats_count}")


car1 = Car('Nissan', 'Skyline', 1990, 'gas')
car2 = Car('Toyota', 'Prius', 2020, 'electricity')
car1.start_engine()
print(car2.__dict__)

moto1 = Motorcycle('Yamaha', 'R1', 2000, 5, True)
moto2 = Motorcycle('Syzyki', 'Spirit', 2012, 8, False)
moto1.info()
moto2.fastest()

bicycle1 = Bicycle('Toster', 'Krawler', 2023, 23, 1)
bicycle2 = Bicycle('Hamwee', 'Wrangler', 2001, 27, 2)
bicycle1.info()
bicycle2.info()