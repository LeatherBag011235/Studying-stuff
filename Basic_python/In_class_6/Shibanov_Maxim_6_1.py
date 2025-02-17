class Car:

    def __init__(self, layout: str, color: str):
        self.layout = layout
        self.color = color
        print(f"This car is {self.color} {self.layout}")

my_car = Car('SUV', "White")
another_car_1 = Car('SUV', "Green")
another_car_2 = Car('Sedan', "Yelow")
another_car_3 = Car('SUV', "Red")
another_car_4 = Car('Sedan', "Blue")