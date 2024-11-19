"""
Завдання 4: Принцип розділення інтерфейсу користувача (Interface Segregation Principle - ISP)

Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання. 
Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. 
Переконайтеся, що жоден з класів не має пустого методу.
"""

# Пояснення - кожна функціональність описується в окремому класі та використовується лише там де потрібно (для сканеру не потрібна функціональність друк)


class Printable():
    def printing(self):
        raise NotImplementedError("Method printing has not implemented")

class Scannable():
    def scanning(self):
        raise NotImplementedError("Method scanning has not implemented")
    
class Copyable():
    def copying(self):
        raise NotImplementedError("Method copying has not implemented")

class NetworkPrinter(Printable, Scannable, Copyable):

    def printing(self):
        print('Now the network printer is printing')

    def scanning(self):
        print('Now the network printer is scanning')
    
    def copying(self):
        print('Now the network printer is copying')


class Printer(Printable):
    
    def printing(self):
        print('Now the printer is printing')


class Scanner(Scannable):

    def scanning(self):
        print('Now the scanner is scanning')


printer1 = Printer()
printer1.printing()

scanner1 = Scanner()
scanner1.scanning()

newtwork_printe1 = NetworkPrinter()
newtwork_printe1.printing()
newtwork_printe1.scanning()
newtwork_printe1.copying()