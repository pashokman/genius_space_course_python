"""
**Завдання 1: Створення класу і об'єктів**

Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:

- `name` (ім'я тварини)
- `species` (вид тварини)
- `age` (вік тварини)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.
"""


class Animal:

    def __init__(self, name:str, species:str, age:float, sound:str):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.sound)

animal1 = Animal('Tasker', 'Dog', 5, 'Gav Gav Gav')
animal2 = Animal('Miki', 'Mouse', 2.5, 'Mi Mi Mi')

animal1.make_sound()
animal2.make_sound()