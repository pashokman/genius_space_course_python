"""
Завдання 1: Інкапсуляція
Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
Ім'я (name)
Електронна пошта (email)
Пароль (password)
Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). 
Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.
"""

class User():

    def __init__(self, name:str, email:str, password:str):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_attribute(self, attribute_name:str):
        return self.__dict__[f"_{self.__class__.__name__}__{attribute_name}"]

    def set_attribute(self, attribute_name:str, value:str):
        self.__dict__[f"_{self.__class__.__name__}__{attribute_name}"] = value


user1 = User("Jane", "jane@mail.com", "TestPassword123")
print(user1.get_attribute("name"))
print(user1.get_attribute("email"))
print(user1.get_attribute("password"))

user1.set_attribute("name", "Lana")
print(user1.get_attribute("name"))
user1.set_attribute("email", "lana@mail.com")
print(user1.get_attribute("email"))
user1.set_attribute("password", "TestPassword321")
print(user1.get_attribute("password"))