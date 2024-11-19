"""
**Завдання 1: Робота з функціями**

Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:

1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. 
Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. 
Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.
"""


from calculator import *


def calculate(a, b, sign):
    if sign == '+':
        print(add(a, b))
    elif sign == '-':
        print(subtract(a, b))
    elif sign == '*':
        print(multiply(a, b))
    elif sign == '/':
        print(divide(a, b))
    else:
        print('The sign is incorrect, try again!')

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
sign = str(input("Enter operation sign: "))

calculate(a, b, sign)