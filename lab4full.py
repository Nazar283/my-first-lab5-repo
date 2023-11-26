
class Printer:
    def __init__(self, name, print_speed, price):
        self.__name = name
        self.__print_speed = print_speed
        self.__price = price
        self.name = name
        self.price = price

    def get_name(self):
        return self.__name

    def get_print_speed(self):
        return self.__print_speed

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_print_speed(self, print_speed):
        self.__print_speed = print_speed

    def set_price(self, price):
        self.__price = price

    # def __str__(self):
    #     return f"Printer: {self.__name}, Speed: {self.__print_speed} pages per minute, Price: {self.__price} UAH"

    def __repr__(self):
        return f"Printer('{self.__name}', {self.__print_speed}, {self.__price})"

    def __del__(self):
        print(f"The printer {self.__name} has been deleted.")  #деструктор

printer1 = Printer("HP LaserJet", 40, 560)     #класи
printer2 = Printer("Epson EcoTank", 25, 600)
printer3 = Printer("Canon Pixma", 20, 350)

print(printer1)
print(printer2)
print(printer3)