"""
Завдання 2: Абстракція
Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). 
У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        return (self.a + self.b + self.c) / 2
    

circle1 = Circle(5)
print("Circle area:", circle1.calculate_area())

rectangle1 = Rectangle(5, 6)
print("Rectangle area:", rectangle1.calculate_area())

triangle1 = Triangle(4, 5, 6)
print("Triangle area:", triangle1.calculate_area())
