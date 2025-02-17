class CarFactory:

    company_name: str = "ABC Motors"

    def __init__(self, type: str, color: str):
        self.type = type
        self.color = color
        print(f"This car is {self.color} {self.type}, produced by: {CarFactory.company_name}")

my_car = CarFactory('SUV', "White")
another_car_1 = CarFactory('Hatchback', "Green")
another_car_2 = CarFactory('Sedan', "Yelow")
another_car_3 = CarFactory('SUV', "Red")
another_car_4 = CarFactory('Sedan', "Blue")

CarFactory.company_name = "XYZ Road Machines"