"""
**Завдання 2: Поліморфізм**

Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб 
(наприклад, "Це [виробник] [модель] [рік] року виробництва.").

В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.

Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, 
як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.
"""


class Vehicle:

    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year

    
    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")


class Car(Vehicle):

    def __init__(self, make, model, year, fuel_type:str):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print("Engine is running.")

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва, що працює на паливі - {self.fuel_type}.")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, speeds:int, mod_exhaust:bool):
        super().__init__(make, model, year)
        self.speeds = speeds
        self.mod_exhaust = mod_exhaust

    def fastest(self):
        print("This transport is the fastest.")

    def display_info(self):
        msg = f"Це {self.make} {self.model} {self.year} року виробництва, з {self.speeds} передачами"
        if self.mod_exhaust == True:
            print(msg + " та модифікованим вихлопом.")
        else:
            print(msg + " та стовим вихлопом.")


class Bicycle(Vehicle):

    def __init__(self, make, model, year, wheel_radius:int, seats_count:int):
        super().__init__(make, model, year)
        self.wheel_radius = wheel_radius
        self.seats_count = seats_count

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва з колесами {self.wheel_radius} радіусу та {self.seats_count} сидінням(и).")


car1 = Car('Nissan', 'Skyline', 1990, 'gas')
car2 = Car('Toyota', 'Prius', 2020, 'electricity')
car1.start_engine()
print(car2.__dict__)

moto1 = Motorcycle('Yamaha', 'R1', 2000, 5, True)
moto2 = Motorcycle('Syzyki', 'Spirit', 2012, 8, False)
moto1.display_info()
moto2.fastest()

bicycle1 = Bicycle('Toster', 'Krawler', 2023, 23, 1)
bicycle2 = Bicycle('Hamwee', 'Wrangler', 2001, 27, 2)
bicycle1.display_info()
bicycle2.display_info()