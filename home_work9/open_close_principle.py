"""
Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)

Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). 
Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. Використовуйте принцип OCP для розширення функціональності.
"""

# Створивши клас Shape ми в ньому вказали які методи обов'язково мають бути реалізовані у класах нащадках.
# Ми створили окремий клас CalculateArea, який може обчислити площу будь якої з фігур в коді - цей клас не змінює функціональність існуючих класів, а розширює її.
# Таким чином, існуючі класи залишаються незмінними, і система легко розширюється шляхом додавання нових підкласів.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
class CalculateArea():
    
    @staticmethod
    def calculate_area(shape: Shape):
        return shape.area()
        

circle1 = Circle(3)
rectangle1 = Rectangle(5, 6)

area_calculator = CalculateArea()

circle1_area = area_calculator.calculate_area(circle1)
print(f"Area of {circle1.__class__.__name__} = {circle1_area:.2f}")

rectangle1_area = area_calculator.calculate_area(rectangle1)
print(f"Area of {rectangle1.__class__.__name__} = {rectangle1_area:.2f}")

