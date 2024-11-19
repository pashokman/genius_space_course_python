"""
**Завдання 2: Робота з об'єктами**

Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:

- `width` (ширина прямокутника)
- `height` (висота прямокутника)

Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).

Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.
"""


class Rectangle:

    def __init__(self, width:float, height:float):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(2.5, 4)

print(rectangle1.calculate_area())
print(rectangle2.calculate_area())