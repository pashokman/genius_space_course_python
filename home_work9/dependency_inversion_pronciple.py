"""
Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)
Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, щоб він використовував абстракції та інтерфейси замість конкретних реалізацій. 
Переконайтеся, що класи залежностей не знають про конкретну реалізацію інших класів.
""" 


from abc import ABC, abstractmethod

# Абстрактний інтерфейс для всіх служб повідомлень
class MessageService(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

# Конкретна реалізація служби Email
class EmailService(MessageService):
    def send_message(self, recipient, message):
        print(f"Відправлення Email до {recipient}: {message}")

# Конкретна реалізація служби SMS
class SMSService(MessageService):
    def send_message(self, recipient, message):
        print(f"Відправлення SMS до {recipient}: {message}")

# Клас NotificationService залежить від абстракції, а не від конкретної реалізації
class NotificationService:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def notify(self, recipient, message):
        self.message_service.send_message(recipient, message)


email_service = EmailService()
sms_service = SMSService()

notification_service = NotificationService(email_service)
notification_service.notify("user@example.com", "Привіт через Email!")

notification_service_sms = NotificationService(sms_service)
notification_service_sms.notify("+1234567890", "Привіт через SMS!")