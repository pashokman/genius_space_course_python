"""
Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)

Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" без порушення функціональності. 
Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.
"""

# Пояснення - у кожному з підкласів було реалізовано обов'язкові методи батківського класу,
# було створено метод, який приймає об'єкт типу Shape та коректно працює з будь яким підкласом
# Таким чином, кожен підклас може замінити базовий клас без порушення функціональності.


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass

class Rectangle(Shape):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimetr(self):
        return self.a * 2 + self.b * 2
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2    
    
    def perimetr(self):
        return 2 * pi * self.radius
    

def shape_info(shape):
    print(f"Area of {shape.__class__.__name__} = {shape.area():.2f}")
    print(f"Perimetr of {shape.__class__.__name__} = {shape.perimetr():.2f}")


rectangle1 = Rectangle(3, 4)
circle1 = Circle(2)

shape_info(rectangle1)
shape_info(circle1)