"""
Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)

Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. 
В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача. 
Переконайтеся, що кожен метод відповідає за одну конкретну функцію.
"""

class User:

    id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.increment_id()

    def increment_id(self):
        User.id += 1
        return User.id
    
    def change_name(self, name):
        def_name = self.name
        self.name = name
        print(f"Name {def_name} was changed to {self.name}")


class UserManager():

    def __init__(self):
        self.users = {}

    def create_user(self, name):
        user = User(name)
        self.users[user.id] = user
        print(f"User {user.name} created! Hiw id = {user.id}")
        return user

    def update_user(self, user_id, name):
        user = self.users.get(user_id)
        if user:
            user.change_name(name)
            return user
        else:
            print("User does not exist!")

    def delete_user(self, user_id):
        user = self.users.get(user_id)
        if user:
            del self.users[user_id]
            print(f"User {user.name} with id = {user_id} deleted!")
        else:
            print("User does not exist!")


manager = UserManager()

user1 = manager.create_user("James")
user2 = manager.create_user("Lucas")

manager.update_user(user1.id, "Jameson")

manager.delete_user(user1.id)
