"""
### Списки:
1. **Робота із списками:**
Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.
"""
print('Lists')
print('Task 1')
first_list = [1, 2, 3, 4, 5]
print(first_list)
first_list.append(10)
print(first_list)
first_list.insert(3, 20)
print(first_list)
first_list.remove(10)
print(first_list)
print()

"""
2. **Знаходження суми:**
Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.
"""
print('Task 2')
numbers_list = [1, 3, 5, 7, 9]
print(sum(numbers_list))
print()

"""
3. **Подвійні значення:**
Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
"""
print('Task 3')
new_numbers_list = [1, 2, 3, 4, 5, 6]
print(new_numbers_list)
result_list = []

for i in new_numbers_list:
    result_list.append(i * 2)

print(result_list)
print()

"""
### Кортежі:
1. **Робота із кортежами:**
Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин"). Виведіть кожен елемент кортежу окремо.
"""
print('Tuples')
print('Task 1')
new_tuple = ("яблуко", "банан", "апельсин")
for i in new_tuple:
    print(i)
print()

"""
2. **Об'єднання кортежів:**
Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.
"""
print('Task 2')
first_tuple = (1, 2, 3, 4)
print(first_tuple)
second_tuple = (5, 6, 7, 8)
print(second_tuple)

third_tuple = first_tuple + second_tuple
print(third_tuple)
print()

"""
### Словники:
1. **Робота із словниками:**
Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.
"""
print('Dictionaries')
print('Task 1')
athlete = {
    "name": "Vasily",
    "age": 50,
    "sport": "Strongman",
    "team": "Ukraine"
}
print(athlete)
print(f"Athlete name: {athlete.get('name')}, his age: {athlete.get('age')}, his sport: {athlete.get('sport')} and his team: {athlete.get('team')}.")
print()

"""
2. **Оновлення словника:**
Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). Додайте до словника нову улюблену книгу та виведіть оновлений словник.
"""
print('Task 2')
books = {
    "The Witcher": 1990,
    "The Last Wish": 1993,
    "Sword of Destiny": 1992,
    "Blood of Elves": 1994
}
print(books)
books['Time of Contempt'] = 1995
print(books)
print()

"""
3. **Пошук значення:**
Завдання: Створіть словник, що містить інформацію про країни та їх столиці. Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
"""
print('Task 3')
countries = {
    "Ukraine": "Kyiv",
    "USA": "Washington",
    "Netherlands": "Amsterdam",
    "Germany": "Berlin"
}
asked_country_name = "Germany"
print(countries.get(asked_country_name))
