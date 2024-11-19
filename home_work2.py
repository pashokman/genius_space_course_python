"""
1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None
2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
"""
# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None

message_str = "Skyline"
print(type(message_str))

number_int = 87
print(type(number_int))

number_float = 45.9
print(type(number_float))

is_something_bool = True
print(type(is_something_bool))

ages_list = [5, 12.5, 70, 38]
print(type(ages_list))

car_dict = {
    'vendor': 'Nissan', 
    'model': message_str, 
    'production_year': 1998,
    'is_on_sale': is_something_bool,
    'engine_capacity_liters': 2.8,
    'transmission': 'manual',
    'speeds_count': 5,
    'color': 'black'
    }
print(type(car_dict))

some1_tuple = ('Kate', 75, True, 'val')
print(type(some1_tuple))

important_variable_none = None
print(type(important_variable_none))
print()


# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі
# Порівняння чисел
print('Int number is greater than float: ', number_int > number_float)
print('Int number is less than float: ', number_int < number_float)
print('Int number is equal to float: ', number_int == number_float)
print('Int number is not equal to float: ', number_int != number_float)
print()

# Порівняння рядків
print("Message is not equal to car vendor: ", message_str != car_dict['vendor'])
print("Message is equal to car model: ", message_str == car_dict['model'])
print("Message is greater than car vendor: ", message_str > car_dict['vendor'])
print("Message is less than car vendor: ", message_str < car_dict['vendor'])
print()

# Порівняння булевих значень
print("Is something greater than car is on sale: ", is_something_bool > car_dict['is_on_sale'])
print("Is something less than car is on sale: ", is_something_bool < car_dict['is_on_sale'])
print("Is something equal to car is on sale: ", is_something_bool == car_dict['is_on_sale'])
print("Is something not equal to car is on sale: ", is_something_bool != car_dict['is_on_sale'])
print()

# Порівняння списків
new_list = [5, 12.5, 70, 38, 37]
print("List ages is greater than new list: ", ages_list > new_list)
print("List ages is less than new list: ", ages_list < new_list)
print("List ages is equal to new list: ", ages_list == new_list)
print("List ages is not equal to new list: ", ages_list != new_list)
print("List ages is in new list: ", ages_list in new_list)
print("List ages is not in new list: ", ages_list not in new_list)
print("First element of list ages is not in new list: ", ages_list[0] not in new_list)
print("First element of list ages is in new list: ", ages_list[0] in new_list)
print()

# Порівняння словників
person_dict = {
    'name': 'Alice',
    'age': 35,
    'hair_color': 'black',
    }
print("Dictionary car model is not equal to the dicionary person name: ", car_dict['model'] != person_dict['name'])
print("Dictionary car color is equal to the dicionary person hair color: ", car_dict['color'] == person_dict['hair_color'])
print("Person dict has age property: ", 'age' in person_dict)
print("Person dict has male property: ", 'male' in person_dict)
print()

# Порівняння кортежів
some2_tuple = ('Kate', 75, True, 'val')
some3_tuple = ('Kate', 75, True, 'val', (1, 'two'))
some4_tuple = (1, 'two')
some5_tuple = (1, 'nice', 'job')
print("Tuple 2 is equal to tuple 1: ", some2_tuple == some1_tuple)
print("Tuple 3 is not equal to tuple 1: ", some3_tuple != some4_tuple)
print("Typle 4 is in tuple 3: ", some4_tuple in some3_tuple)
print("Tuple 2 is equal to tuple 1 and tuple 4 is in tuple 3: ", some2_tuple == some1_tuple and some4_tuple in some3_tuple)
print("Tuple 2 is equal to tuple 1 or tuple 4 is in tuple 5: ", some2_tuple == some1_tuple or some4_tuple in some5_tuple)
print()

"""
3. Використати вивчені функції Python:
Робота з рядками:
 1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
 2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити  
усі букви 'y' на '0' та 'i' на '1'.
 3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
 4. Визначити довжину рядку string_join за допомогою функції len()
"""
num_str = 125
print(type(num_str))
num_str = str(num_str)
print(type(num_str))

message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)

split_test = 'This is a split test'
print(split_test)
split_test = split_test.split()
print(split_test)
string_join = ' '.join(split_test)
print(string_join)
print(len(string_join))
print()

"""
Робота зі списками:
 1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
 2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
 4. Визначити довжину списку list_append за допомогою функції len()
"""
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))

print(len(list_append))
print()

"""
Робота зі словниками:
 1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
 2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
 3. За допомогою функції items() вивести на екран пари ключ - значення
"""

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())
