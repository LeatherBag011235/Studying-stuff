import math 

class ScientificCalculator:

    def __init__(self):
        self.results = []
    
    def add(self, a: float, b: float):
        res = a + b
        self.results.append(res)
        return self.results[-1]
    
    def subtract(self, a: float, b: float):
        res = a - b
        self.results.append(res)
        return self.results[-1]
    
    def multiply(self, a: float, b: float):
        res = a * b
        self.results.append(res)
        return self.results[-1]
    
    def divide(self, a: float, b: float):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        res = a / b
        self.results.append(res)
        return self.results[-1]
    
    def exp(self, a: float):
        res = math.exp(a)
        self.results.append(res)
        return self.results[-1]
    
    def power(self, a: float, p: float):
        """
        This method raises a: float to the power of p: float.
        E.g. this function allow you to take roots as well.
        Note that in case p < 1 => a must be positive.
        """
        if p < 1 and a < 0:
            raise ValueError("For negative 'a', 'p' must be ≥ 1 to avoid complex results.")

        res = a ** p
        self.results.append(res)
        return self.results[-1]

    def display(self):
        print('\n')
        if self.results:
            print(f"Last results: {self.results[-3:]}")
            print(f"Total operations: {len(self.results)}")
        else:
            print("No results yet")

    def display_all(self):
        print('\n')
        if len(self.results) > 0:
            print(f"All results: {self.results}")
            print(f"Total operations: {len(self.results)}")
        else:
            print("No results yet")

    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compute(self):
        while True:
            self.display()

            while True:
                try:
                    operation = int(input(
                        "Chose and operation:\n"
                        "1. add\n2. subtruct \n3. multiply \n4. divide \n5. exponent \n6. power \n7. display all results \n8. exit \n"
                        "Input a corresponding integer:(1/2/3/4/5/6/7)"
                        ))
                    
                    if 1 <= operation <= 8:
                        break 
                    else:
                        print("An input should be an integer number from 1 to 8")
                except ValueError:
                    print("An input should be an integer number from 1 to 8")

            if operation == 1:
                a = ScientificCalculator.get_float_input("Input first term for addition")
                b = ScientificCalculator.get_float_input("Input second term for addition")
                print(self.add(a, b))

            elif operation == 2:
                a = ScientificCalculator.get_float_input("Input first term for subtruction")
                b = ScientificCalculator.get_float_input("Input second term for subtruction")
                print(self.subtract(a, b))

            elif operation == 3:
                a = ScientificCalculator.get_float_input("Input first term for multiplication")
                b = ScientificCalculator.get_float_input("Input second term for multiplication")
                print(self.multiply(a, b))

            elif operation == 4:
                a = ScientificCalculator.get_float_input("Input first term for division")
                b = ScientificCalculator.get_float_input("Input second term for division")
                print(self.divide(a, b))

            elif operation == 5:
                a = ScientificCalculator.get_float_input("Input the power for exponent")
                print(self.exp(a))

            elif operation == 6:
                a = ScientificCalculator.get_float_input("Input the base")
                p = ScientificCalculator.get_float_input("Input the power")
                print(self.power(a, p))

            if operation == 7:
                self.display_all()

            if operation == 8:
                self.display_all()
                break
        