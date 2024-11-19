"""
Блок бібліотеки requests:

Завдання 1: Виконання GET-запиту
Створіть Python-сценарій, який використовує бібліотеку requests для виконання GET-запиту до веб-ресурсу та виведення вмісту веб-сторінки на екран. 
Використовуйте функцію requests.get() для виконання запиту.

Завдання 2: Параметри запиту
Розширте попереднє завдання, додаючи можливість вказати параметри запиту. Виконайте GET-запит до веб-ресурсу, 
передаючи параметри запиту, такі як параметри запиту у URL або параметри через словник.

Завдання 3: POST-запит
Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу. Відправте дані на сервер, наприклад, форму з ім'ям користувача і паролем.

Завдання 4: Обробка відповіді
Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть потрібну інформацію. Наприклад, виведіть заголовки відповіді або вміст сторінки.

Завдання 5: Обробка помилок
Додайте обробку помилок до вашого коду. Обробляйте можливі винятки, такі як requests.exceptions.RequestException, та виводьте відповідні повідомлення про помилку.

Завдання 6: Збереження вмісту в файл
Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл. Використайте функціонал Python для роботи з файлами для збереження вмісту.
"""

import requests


host = "https://restful-booker.herokuapp.com/"


# Task 1
response_get = requests.get(host + "/booking")
print(response_get.text)
print("----------------------------")

# Task 2
some_booking_id = f"/booking/{1}"
response_get = requests.get(host + some_booking_id)
print(response_get.text)
print("----------------------------")

# Task 3
new_booking = {
    "firstname": "Sally",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-02-23",
        "checkout": "2025-10-23"
    },
    "additionalneeds": "Breakfast"
}

response_post = requests.post(host + "/booking", json=new_booking)
print(response_post.status_code)
print(response_post.text)
print("----------------------------")

# Task 4
def resp_post_parser(resp):
    try:
        if resp.status_code >= 200 and resp.status_code < 300:
            j = resp.json()
            print(f"Operation successful! Booking order id - {j['bookingid']}.")
            print(f"Thanks for the order, {j['booking']['firstname']} {j['booking']['lastname']}!")
        else:
            raise requests.exceptions.RequestException(f"Something goes wrong! Status code - {resp.status_code}, error msg - {resp.text}")
    except Exception as e:
        print(f"Some error occured - {e}")

resp_post_parser(response_post)

# Task 5
# incorrect request

response_post2 = requests.post(host + "/booking")
resp_post_parser(response_post2)

# Task 6

with open('test_file.txt', 'w') as file:
    file.write(response_post.text)
