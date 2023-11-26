class Printer:
    def __init__(self, name, print_speed, price):
        self.name = name 
        self.print_speed = print_speed
        self.price = price

    def print_info(self):
        print(f"Принтер: {self.name}")
        print(f"Швидкість друку: {self.print_speed} сторінок/хв")
        print(f"Ціна: {self.price} грн")

printer1 = Printer("HP LaserJet", 30, 2000)
printer2 = Printer("Canon Pixma", 25, 1350)

printer1.print_info()
printer2.print_info()