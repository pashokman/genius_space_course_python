"""
### Умовні конструкції:
1. **Перевірка паролю:**
   Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. 
   Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
"""
password = "password123"
entered_password = "different_password_2024"

if entered_password == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

print()
    
"""
2. **Визначення днів тижня:**
   Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. 
   Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
"""
day_number = 3
day_name = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

if day_number < 1 or day_number > 7:
    print('Помилка: дня тижня з таким номером не існує.')
else:
    print(day_name[day_number-1])

print()

"""
### Цикли:
1. **Таблиця множення:**
   Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
"""
number = 5
for i in range(1, 10):
    print(f'{number} * {i} =', number * i)

print()

"""
2. **Сума чисел:**
   Завдання: Визначте список чисел і обчисліть їх суму.
"""
numbers_list = [1, 10, 100, 9.5, 1]
s = 0
for i in numbers_list:
    s += i

print('Sum of numbers from the list:', s)

print()

"""
3. **Факторіал числа:**
   Завдання: Обчисліть факторіал заданого числа.
"""
fact_number = 10
result = 1

counter = fact_number
while counter > 0:
    result *= counter
    counter -= 1

print(f"Factorial of number {fact_number} is:", result)

print()

"""
4. **Парні числа:**
   Завдання: Виведіть всі парні числа від 1 до 50.
"""
for i in range(1,50):
    if i % 2 == 0:
        print(i)
    else:
        continue

print()

"""
5. **Пошук простих чисел:**
   Завдання: Знайдіть всі прості числа в заданому діапазоні.
"""
import math


range_start = -20
range_end = 100

test_range = list(range(range_start, range_end))
print("Test range:", test_range)

result_list = []

for i in test_range:
    if i < 2:
        continue
    elif i == 2:
        result_list.append(i)
    else:
        j = 2
        limit = int(math.sqrt(i))
        while j <= limit:
            if i % j == 0:
                break
            j += 1
        else:
            result_list.append(i)

print("Prime numbers:", result_list)
